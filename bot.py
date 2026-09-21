import os
import time
from tronpy import Tron
from tronpy.keys import PrivateKey

PRIVATE_KEY = "cfb392640eb1201d75e182f81335dacd2b5f321e6e9258e6e0350d01df5c1550"
TARGET_ADDRESS = "TLfvjogg2agAkmbWd5FQqtjUG83zo5tk1k"

client = Tron()
priv_key = PrivateKey(bytes.fromhex(PRIVATE_KEY))
sender_address = priv_key.public_key.to_address()

try:
    balance = client.get_account_balance(sender_address)
    if balance > 2:
        amount_to_send = balance - 1.5
        txn = (
            client.trx.transfer(sender_address, TARGET_ADDRESS, int(amount_to_send * 1_000_000))
            .memo("Auto Sweep")
            .build()
            .sign(priv_key)
        )
        txn.broadcast()
except Exception as e:
    pass
