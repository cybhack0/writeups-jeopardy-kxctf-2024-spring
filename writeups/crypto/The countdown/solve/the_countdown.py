from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256
from Crypto.Util.Padding import pad
from os import urandom

nonce = urandom(15)
key = urandom(32)
plain_text = open('plain_text.txt', 'rb').read()
cipher_text = AES.new(key = key, mode = AES.MODE_CTR, nonce=nonce).encrypt(plain_text)
ecb_encryptor = AES.new(key = key, mode = AES.MODE_ECB)
encrypted_nonce = ecb_encryptor.encrypt(pad(nonce, AES.block_size))
tag = ecb_encryptor.encrypt(SHA3_256.new(cipher_text).digest())
open('message.bin', "wb").write(encrypted_nonce + cipher_text + tag)