import sys, os, re, requests, jsonrpclib

from decimal import *

access = jsonrpclib.Server("http://doge:wow@127.0.0.1:22555")
#print(access.getinfo())

if len(sys.argv) < 3:
	sys.exit("Usage: %s <dogecoin address> <amount>" % sys.argv[0])

fromAddress = 'DCCpdXmwD9TjqnXvmm7NrrBQt2nBKEPDSt'
toAddress = sys.argv[1]
amount = sys.argv[2]
TRANSACTION_TAX = Decimal('0.001') # should be changed to actual number

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

print balance
print "SENDING: %d" % amount