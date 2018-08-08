#!/bin/env python

from pwn import *

conn = remote('pwnable.kr', 9007)
print conn.recv()

for i in range(0,100):
	conn.sendline(str(i))
	print conn.recv(1024, timeout=0.2)

print conn.recv(1024, timeout=1)
conn.close()
