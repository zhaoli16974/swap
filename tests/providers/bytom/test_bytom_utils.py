#!/usr/bin/env python3

from shuttle.providers.bytom.wallet import Wallet
from shuttle.providers.bytom.utils import sign, verify


def test_bytom_sign_and_verify():
    wallet = Wallet(network="mainnet",  account=1, change=False, address=1)\
        .from_mnemonic("indicate warm sock mistake code spot acid ribbon sing over taxi toast")
    private_key = wallet.private_key()
    public_key = wallet.public_key()
    # Message or Unsigned data
    message = "ecaba401a6df9cffbed37d1abcf23b91b3c84ec7aa9411d481cbef2e437ef7b1"

    signature = sign(private_key, message)
    assert signature == "5bd906d6829b1679c1b6e987849e5f8432a1dd7114b026908f675dafb9a9526e25a7a23f451e08695c133e67a89" \
                        "9079cf75410cc055b937158fc473e8154130a"

    assert verify(public_key, signature, message)