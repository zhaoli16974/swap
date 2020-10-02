#!/usr/bin/env python3

from swap.providers.bitcoin.htlc import HTLC
from swap.providers.bitcoin.rpc import get_balance
from swap.utils import sha256

# Bitcoin network
NETWORK: str = "testnet"
# Secret password/passphrase hash
SECRET_HASH: str = sha256("Hello Meheret!")
# Recipient Bitcoin address
RECIPIENT_ADDRESS: str = "mgokpSJoX7npmAK1Zj8ze1926CLxYDt1iF"
# Sender Bitcoin address
SENDER_ADDRESS: str = "mkFWGt4hT11XS8dJKzzRFsTrqjjAwZfQAC"
# Expiration block (Sequence)
SEQUENCE: int = 1000

print("=" * 10, "Hash Time Lock Contract (HTLC) between Sender and Recipient")

# Initialize Bitcoin HTLC
htlc: HTLC = HTLC(network=NETWORK)
# Build HTLC contract
htlc.build_htlc(
    secret_hash=SECRET_HASH,
    recipient_address=RECIPIENT_ADDRESS,
    sender_address=SENDER_ADDRESS,
    sequence=SEQUENCE,
)

# Print all HTLC info's
print("HTLC Bytecode:", htlc.bytecode())
print("HTLC OP_Code:", htlc.opcode())
print("HTLC Hash:", htlc.hash())
print("HTLC Address:", htlc.address())

# Get HTLC balance
print("HTLC Balance:", get_balance(
    address=htlc.address(), network=NETWORK
))
