#!/usr/bin/python
"""
reimbursement script version 0.1

USAGE: python reimburse.py <address to send to> <amount to send>

CAUTION: this script must be used on a computer with dogecoind running.
amounts sent will be deducted from the wallet associated with dogecoind

TODO: connect to MySQL database instead of using manual text entry.
	  get dogecoind running on same server as MySQL database
	  scrub all sensitive info so this can be open sourced :P

"""
import sys, os, re, requests, jsonrpclib, MySQLdb

from decimal import *

TRANSACTION_TAX = Decimal('1.0') # is this right?

# set up necessary accesses...
access = jsonrpclib.Server("http://doge:wow@127.0.0.1:22555")
db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
cursor = db.cursor()

# get data from db...
sql = "SELECT * FROM CLAIMS"

try:
	# Execute SQL command
	cursor.execute(sql)
	# Fetch ALL the rows!
	results = cursor.fetchall()
	for row in results:
		toAddress = row[1]
		amount = row[2]
		if type(amount) != Decimal:
			amount = Decimal(amount)

		#rounds so that there are no infinitely long numbers to deal with
		amount = amount.quantize(Decimal('0.000000001'))
		amount += TRANSACTION_TAX

		toValid = access.validateaddress(toAddress)['isvalid']

		if not toValid:
			print 'toAddress or fromAddress not valid'
			break

		if amount > 50000:
			print "Withdrawal amount: %d" % amount
			print 'Requested withdrawal was too large'
			break

		try:
			access.sendtoaddress(toAddress,float(amount))
			print "SENDING: %d to %s" % (amount, toAddress)
		except Exception, e:
			print 'Inusfficient funds to complete transaction'
			break
except:
	print "Error: unable to fetch data from db"

db.close()









