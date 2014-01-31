#!/usr/bin/python
"""
The MIT License (MIT)

Copyright (c) 2013 Jon Harrell

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

=======reimbursement script version 1.7==========

USAGE: python reimburse.py

DESCRIPTION: This is an auto-reimbursement script compatible with any bitcoin
derived cryptocurrency that uses a similar structure to bitcoind. This script will
1) Connect to a locally running instance of (in this case) dogecoind, or another altcoin
2) Connect to a locally running MySQL database where the reimbursement amounts and addresses
are held
3) Iterate through the database and reimburse users up to a ratio defined by
REIMBURSEMENT_RATIO. If an amount to reimburse is greater than a set amount (REIMBURSEMENT_CAP)
the user should be manually verified and dealt with instead of in this script. If the ratio calculation
is too low as defined by REIMBURSEMENT_MIN, the amount will be increased to the minimum.
4) Database will be updated to reflect new amount paid to each claim.

NOTE: this script must be used on a computer with dogecoind running.
amounts sent will be deducted from the wallet associated with dogecoind

MYSQL NOTE: rows contained in this database were much larger than what was used here. 
			the most relevant rows are id, estimated_amount_lost, reimburse_addr, and valid.

"""
import sys, os, re, requests, jsonrpclib, MySQLdb

from decimal import *

REIMBURSEMENT_RATIO = Decimal('1.0') # change depending on amount raised
REIMBURSEMENT_CAP = 10000
REIMBURSEMENT_MIN = 10000

# set up necessary accesses...
# change these to match your specifications
rpcuser = "doge"
rpcpassword = "wow"
rpcconnect = "127.0.0.1"
rpcport = "22555"

accessString = "http://%s:%s@%s:%s" % (rpcuser, rpcpassword, rpcconnect, rpcport)
access = jsonrpclib.Server(accessString)
db = MySQLdb.connect(host="localhost",user="root",passwd="",db="test")
cursor = db.cursor()

# get data from db...
# estimated_amount_lost > 0 is necessary as some rows were negative numbers. Possible int overflow or intentional.
# also, rows with 0 will be ignored so no minimum payment will be given to those rows.
sql = "SELECT * FROM claims_processed WHERE valid = 1 AND estimated_amount_lost <= %s AND estimated_amount_lost > 0" % REIMBURSEMENT_CAP

try:
	# Execute SQL command
	cursor.execute(sql)
	# Fetch ALL the rows!
	results = cursor.fetchall()
	for row in results:
		row_id = row[0]
		amt_claimed = row[4]
		toAddress = row[6]
		
		#amount reimbursed and claimed should be stored as decimals
		#to maintain precision.
		if type(amt_claimed) != Decimal:
			amt_claimed = Decimal(amt_claimed)

		#check to see if already reimbursed was removed, as estimated_amount_lost is updated upon reimbursement

		try:
			toValid = access.validateaddress(toAddress)['isvalid']
		except:
			print "Problem accessing dogecoind."
			break

		if not toValid:
			print 'toAddress %s is not valid. Check row_id %d. Skipping reimbursement.' % (toAddress,row_id)
			continue

		# find reimbursement ratio
		owed = amt_claimed * REIMBURSEMENT_RATIO
		if owed < REIMBURSEMENT_MIN:
			print 'Amount to be reimbursed was %d, increasing to %d' % (owed, REIMBURSEMENT_MIN)
			owed = REIMBURSEMENT_MIN

		print "Owed amount: %d" % owed

		if owed > REIMBURSEMENT_CAP:
			print 'Requested withdrawal was too large (owed > %d).' % REIMBURSEMENT_CAP
			print 'Check row id %d associated with address %s' % (row_id, toAddress)
			continue


		#IMPORTANT BLOCK: sending DOGE and updating DB in one try catch block. if either fail, program halts and 
		#user is informed of the location that corrections need to be made to.
		try:
			sql_update = "UPDATE claims_processed SET estimated_amount_lost = %s WHERE id = %s" % ("0", row_id)

			print "SENDING: %d to %s" % (owed, toAddress)
			txid = access.sendtoaddress(toAddress,float(owed)) # converting to float loses precision, but is needed by sendtoaddress
			print "TXID: %s" % txid
			print "UPDATING DB"
			cursor.execute(sql_update)
			db.commit()
		except:
			db.rollback()
			print 'An error occured.'
			print '======INFORMATION======'
			print 'Address: %s' % toAddress
			print 'amount to send: %d' % owed
			print 'row_id: %d' % row_id
			print 'txid: %s' % txid
			#check dogechain.info logs to see if owed was sent.
			print 'total amt to be reimbursed: %d' % amount_claimed
			print '======================='
			break
except:
	print "Error: unable to fetch data from db"

db.close()