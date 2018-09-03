#!/usr/bin/env python

from pwn import *
import math

sh = ssh(host='pwnable.kr',port=2222,user='memcpy',password='guest');
conn = sh.remote('localhost',9022)

print conn.recv()
conn.sendline('8')

for i in range(4,14):
	msg = str(int(math.pow(2,i)) + 8)
	print "msg: " + msg
	conn.sendline(msg)
	print conn.recv()

print conn.recv()
print conn.recv()
