from pwn import *
import re

p = process(['/usr/bin/unzip','37366'])
res = p.recv(timeout=1)
print (res)
p.sendline('5900')
#for i in range(50):
number = re.findall(r'(\d+)\.zip password', res)
print number[0]
p.sendline(number[0])
print p.recv()
