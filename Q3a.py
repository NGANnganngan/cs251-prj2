from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cRFCTSgTES2H5i994CPTcLFwVGmhtMidP4jaNNJcHLNvrS83jyUf')
    #address: mnDdT9kzscia1WxHNAzWLTqadqL83QZqUs
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cTVWd2CnxpaPuGhJmFqzebW86Lz4q6rHmBPjB5NymDjuwTdnhkHy')
    #address: n4on5EkdQKfQD8zBzadHjfGRR9o77JooLD
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cQSEPVEr168L58kD8dFGZy6xafgBcEV8kk9qTWikkDwkufAm7zaY')
    #address: mjxxSwRUH8yf7z4szzKgh4pHzBUuiTzpd2
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        # fill this in!
        OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG, OP_DROP,
        1, cust1_public_key, cust2_public_key, cust3_public_key, 3, OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00011 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '335cd15399d81b9f242219fe9feeb1f3d66f8c776cf6b4a9f5bd815be16cc41b')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
