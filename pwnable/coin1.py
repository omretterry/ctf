#!/usr/bin/env python

from pwn import *
import math

conn = remote('pwnable.kr', 9007)
print conn.recv()
s = conn.recv()

print s
coin_num = int(s.split(' ')[0].split('=')[1])
try_num = int(s.split(' ')[1].split('=')[1])

print 'coin_num:' + str(coin_num) + ' try_num:' + str(try_num)

minindex = 1
maxindex = coin_num

for i in range(100):
	minindex = 0
	maxindex = coin_num

	for j in range(try_num+5):
		#isDouble = (maxindex - minindex + 1) % 2 == 0
		
		middle = (maxindex + minindex) / 2 + (maxindex + minindex) % 2
		#print '##### [middle]:' + str(middle) + '[middle * 2]:' + str(middle * 2)
		#print '<<<<< [min]:' + str(minindex) + ' [max]:' + str(maxindex) + ' [middle]:' + str(middle)
		
		#if isDouble:
		#	left = ' '.join(str(i) for i in range(minindex,middle))
		#else:
		#	left = ' '.join(str(i) for i in range(minindex,middle))
		left = ' '.join(str(i) for i in range(minindex,middle))
		print '>>>>> [left]:' + str(len(left.split(' '))) + '[' + str(minindex) + '-' + str(middle) + ')'
		conn.sendline(left)
		leftres = conn.recv()
		print '<<<<< [leftres]:' + str(leftres)		

		if 'Correct!' in leftres:
			conn.sendline()
			res = conn.recv()
			print res
			coin_num = int(res.split(' ')[0].split('=')[1])
			try_num = int(res.split(' ')[1].split('=')[1])
			conn.recv()
			break
		
		if 'Wrong' in leftres:
			minindex = middle
			continue
		
		#if int(leftres) == 0:
		#	continue
		if int(leftres) % 10 != 0:
		#if int(leftres) < (len(left.split(' ')) * 10):
			maxindex = middle
			print str(minindex) + '~' + str(maxindex)
			continue
		else:
			minindex = middle
			print str(minindex) + '~' + str(maxindex)
			continue
	
		'''
		if isDouble:
			right = ' '.join(str(i) for i in range(middle, maxindex + 1))
		else:
			right = ' '.join(str(i) for i in range(middle, maxindex))
		#print '>>>>> [right]:' + str(len(right.split(' '))) + '[' + str(middle) + '-' + str(maxindex) + ')'
		conn.sendline(right)
		rightres = conn.recv()
		print '<<<<< [rightres]:' + str(rightres)
		
		if leftres > rightres:
			minindex = middle
		else:
			maxindex = middle
		'''


print conn.recv(1024, timeout=1)
conn.close()
