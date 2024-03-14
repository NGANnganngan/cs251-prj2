from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
tong = 5
hieu = 1
Q2a_txout_scriptPubKey = [
        # fill this in!
        OP_OVER, OP_OVER, OP_ADD, tong, OP_EQUAL, OP_DROP, OP_SUB, hieu, OP_EQUAL
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '335cd15399d81b9f242219fe9feeb1f3d66f8c776cf6b4a9f5bd815be16cc41b')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
