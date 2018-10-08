#!/usr/bin/python

import pickle

file=open('donotshare')
file_read=pickle.load(file)

for i in file_read:
	#num = 0
	line = ''
	#print('------------')
	for j in i:
		for k in range(int(j[1])):
			line = line + j[0]
		#num = num + int(j[1])
		#print(j[1])
	#print num
	print line
