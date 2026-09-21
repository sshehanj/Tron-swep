import os
import time
from tronpy import Tron
from tronpy.keys import PrivateKey

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
TARGET_ADDRESS = os.environ.get("TARGET_ADDRESS")

client = Tron()
priv_key = PrivateKey(bytes.fromhex(PRIVATE_KEY))
sender_address = priv_key.public_key.to_address()

print(f"Monitoring Wallet Address: {sender_address}")

while True:
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
            print(f"Successfully Sent {amount_to_send} TRX to {TARGET_ADDRESS}")
            
    except Exception as e:
        pass
    
    time.sleep(2)
