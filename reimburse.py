#!/usr/bin/python
"""
reimbursement script version 0.1

USAGE: python reimburse.py <address to send to> <amount to send>

CAUTION: Make sure that the address listed as 'fromAddress' is the one being
used by this script. ideally, this will be used on a computer with only one
address, that being the one that will be filled to meet the needs of this script

TODO: connect to MySQL database instead of using manual text entry.
	  get dogecoind running on same server as MySQL database
	  scrub all sensitive info so this can be open sourced :P

"""
import sys, os, re, requests, jsonrpclib

from decimal import *

access = jsonrpclib.Server("http://doge:wow@127.0.0.1:22555")


if len(sys.argv) < 3:
	sys.exit("Usage: %s <dogecoin address> <amount>" % sys.argv[0])

#change this to whatever address we will actually be sending from
#fromAddress = 'DCCpdXmwD9TjqnXvmm7NrrBQt2nBKEPDSt'
fromAddress = 'DSqePEZM5xJmz6CcizkcSXnSTZkdRrYPE2'
toAddress = sys.argv[1]
amount = sys.argv[2]
TRANSACTION_TAX = Decimal('1.0') # is this right?

if type(amount) != Decimal:
	amount = Decimal(amount)

#rounds so that there are no infinitely long numbers to deal with
amount = amount.quantize(Decimal('0.000000001'))
amount += TRANSACTION_TAX

fromValid = access.validateaddress(fromAddress)['isvalid']
toValid = access.validateaddress(toAddress)['isvalid']

if not (fromValid and toValid):
	sys.exit('toAddress or fromAddress not valid')

#get the balance of the supplying wallet
balance = requests.get('http://dogechain.info/chain/Dogecoin/q/addressbalance/' + fromAddress)


#convert to decimal
balance = Decimal(balance.text)

if amount >= balance or amount > 50000:
	sys.exit('not enough funds in supplying wallet. Fill \'er up!')

print "BALANCE REMAINING: %d" % (balance - amount)
print "SENDING: %d to %s" % (amount, toAddress)
access.sendtoaddress(toAddress,float(amount))








