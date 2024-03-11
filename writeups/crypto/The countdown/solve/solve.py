message = open('message.bin', 'rb').read()
encrypted_nonce = message[:16]
cipher_text = message[32:48]
flag = bytes(x^y for x,y in zip(encrypted_nonce, cipher_text))
print(flag.decode())