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

=======reimbursement script version 1.1==========

USAGE: python reimburse.py

DESCRIPTION: This is an auto-reimbursement script compatible with any bitcoin
derived cryptocurrency that uses a similar structure to bitcoind. This script will
1) Connect to a locally running instance of (in this case) dogecoind, or another altcoin
2) Connect to a locally running MySQL database where the reimbursement amounts and addresses
are held
3) Iterate through the database and reimburse users up to a ratio defined by
REIMBURSEMENT_RATIO. If an amount to reimburse is greater than a set amount (in this case 50,000)
the user will be flagged and should be manually verified and dealt with instead of in this script.
4) Database will be updated to reflect new amount paid to each claim.

NOTE: this script must be used on a computer with dogecoind running.
amounts sent will be deducted from the wallet associated with dogecoind

MYSQL NOTE: rows should be id, toAddress(varchar 100), amount_reimbursed(decimal(22,9)), amount_claimed(decimal(22,9)), flag(tinyint or bool).
make sure that your table and this code matches. edit if necessary.

TODO: 	further check code for vulnerabilities and inefficiencies.
		scrub all sensitive info so this can be open sourced :P

"""
import sys, os, re, requests, jsonrpclib, MySQLdb

from decimal import *

TRANSACTION_TAX = Decimal('1.0') # is this right?
REIMBURSEMENT_RATIO = Decimal('0.15') # change depending on amount raised
REIMBURSEMENT_CAP = 50000

# set up necessary accesses...
access = jsonrpclib.Server("http://doge:wow@127.0.0.1:22555")
db = MySQLdb.connect(host="localhost",user="root",passwd="",db="testdb") # change this lol
cursor = db.cursor()

# get data from db...
sql = "SELECT * FROM verified_claims WHERE flag = 0"

try:
	# Execute SQL command
	cursor.execute(sql)
	# Fetch ALL the rows!
	results = cursor.fetchall()
	for row in results:
		row_id = row[0]
		toAddress = row[1]
		amount_reimbursed = row[2]
		amount_claimed = row[3]

		#amount reimbursed and claimed should be stored as decimals
		#to maintain precision.
		if type(amount_reimbursed) != Decimal:
			amount_reimbursed = Decimal(amount_reimbursed)
		if type(amount_claimed) != Decimal:
			amount_claimed = Decimal(amount_claimed)

		ratio_reimbursed = ( amount_reimbursed / amount_claimed )
		# Adding this to account for rounding errors, because you never know
		ratio_reimbursed += Decimal("0.00000001") 

		#check to see if already reimbursed
		if ratio_reimbursed >= REIMBURSEMENT_RATIO:
			print "Address %s has already been reimbursed %.2f percent! (%d / %d)" % (toAddress, ratio_reimbursed*100, amount_reimbursed, amount_claimed)
			continue

		owed = ( REIMBURSEMENT_RATIO * amount_claimed ) - amount_reimbursed

		#rounds so that there are no infinitely long numbers to deal with
		#not worried about this, as one Satoshi of a dogecoin makes no difference
		owed = owed.quantize(Decimal('0.000000001'))
		owed += TRANSACTION_TAX
		try:
			toValid = access.validateaddress(toAddress)['isvalid']
		except:
			print "Problem accessing dogecoind."
			break

		if not toValid:
			print 'toAddress %s is not valid. Check row_id %d. Skipping reimbursement.' % (toAddress,row_id)
			continue

		print "Owed amount: %d" % owed
		if owed >= REIMBURSEMENT_CAP:
			print 'Requested withdrawal was too large (owed > %d). Updating flag.' % REIMBURSEMENT_CAP
			sql_flag = "UPDATE verified_claims SET flag = 1 WHERE id = %s" % row_id
			try:
				cursor.execute(sql_flag)
				db.commit()
			except:
				print "Error occured while updating flag. Check row_id %d. Flag should be 1" % row_id
				db.rollback()
				break
			continue


		#IMPORTANT BLOCK: sending DOGE and updating DB in one try catch block. if either fail, program halts and 
		#user is informed of the location that corrections need to be made to.
		try:
			amount_reimbursed += owed
			sql_update = "UPDATE verified_claims SET amount_reimbursed = %s WHERE id = %s" % (amount_reimbursed, row_id)

			print "SENDING: %d to %s" % (owed, toAddress)
			#txid = access.sendtoaddress(toAddress,float(owed)) # converting to float loses precision, but is needed by sendtoaddress
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
			#as amount_reimbursed has been updated, this is what the amount_reimbursed column should be at. 
			#check dogechain.info logs to see if owed was sent.
			print 'total amt to be reimbursed: %d' % amount_reimbursed
			print '======================='
			break
except:
	print "Error: unable to fetch data from db"

db.close()



