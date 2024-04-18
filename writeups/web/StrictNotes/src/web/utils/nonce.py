import time, hashlib

def generate(secret: str) -> str:
    phrase = secret + str(int(time.time()))
    return hashlib.md5(phrase.encode()).hexdigest()