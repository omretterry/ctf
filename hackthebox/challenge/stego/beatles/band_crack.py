from itertools import product
from string import ascii_lowercase
import subprocess
import sys

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 4)]

i = 0
for key in keywords:
	i = i+1
	#print key
	p = subprocess.Popen('unzip -o -P %s BAND.zip' % key, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	#print out,err
	if err.isspace():
		print ">>>>>>>>>>>" 
		print key
		break
	else:
		print "<<<<<<<<<<<"
		pass
	#print("Cracking... " + "[" + str(i) + "/" + str(len(keywords)) + "]")
	#sys.stdout.flush()

'''
p=subprocess.Popen('unzip -o -P 1234 BAND.zip',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = p.communicate()
print out
'''
