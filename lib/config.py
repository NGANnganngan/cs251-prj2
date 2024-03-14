from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

# faucet_address = CBitcoinAddress('mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78')
faucet_address = CBitcoinAddress('tb1qerzrlxcfu24davlur5sqmgzzgsal6wusda40er')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://testnet-faucet.mempool.co/

my_private_key = CBitcoinSecret(
    'cUtJYLGx8akxBLNQL4fTq74nwR9YxzQVxhVJ5Dj79Zhv3WrD57QF')
    # address: mqUEiWf9xKv1aiGJA4PZSSps4jNQa8YBzH

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://testnet-faucet.mempool.co/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cW4mXAMubF7afGZi1HwFpp9ngcKt4B36dPFeta232JgkvqAsdexN')
    #address: msZRtZS1f7T4azywspgZbACJm9cyMik7jh

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cQ1JERX7yxdwh8LukMBns79g3NownSzCXWfATT3ujnGeb8SHWvoa')
    #address: mh4SUXFMsefTjr6QbwkSp8BpgCpcUhaYuC
# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=YOURTOKEN
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('ac5d4b86e90323be2d91e7de74e4bf865611e201c7690fe996af0a001421c305'))
    # {
    #     "private": "ac5d4b86e90323be2d91e7de74e4bf865611e201c7690fe996af0a001421c305",
    #     "public": "036317e398770a71c1c1ecde9c02061aa9055971dc0abcf3b948f73edacb78e4c6",
    #     "address": "BvPgYz3Z3cXssg3qgwzfeLGSevgUXYicSg",
    #     "wif": "Bu75sDmgHqTe6cSWWVetakV8DbE1tQb6Ym6nokYEX6AKgPZpwDCU"
    # }

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('091095425f40c6d196f5dcf85a9741d6b282d9d2cf13bc95cd17e8d5de2e28eb'))
    # {
    #     "private": "091095425f40c6d196f5dcf85a9741d6b282d9d2cf13bc95cd17e8d5de2e28eb",
    #     "public": "03754d31635280b2def89346e6959143c36df65d75acb078d36bba176cc5b39a08",
    #     "address": "CE9eZcjZu5BWu5zauriLokert6eBvejd7i",
    #     "wif": "Bodejxhrnobs9rDyHzHpN6RaTzYgqb8RCVFGozFNZHEUDVcKE3QS"
    # }

    # "tx_ref": "0c6868f8fdffc09281f96cab49c3d33d0cbef61ff68a746776b720d9962132e2"

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################
