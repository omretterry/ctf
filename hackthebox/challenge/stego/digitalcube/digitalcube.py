f=open('digitalcube.txt')
#letter_num = 0
#line_num = 0
#for line in f.readlines():
#	line_num = line_num + 1
#	letter_num = letter_num + len(line)	
#print letter_num,line_num
line = f.readline().strip()
#print line
def splitCount(s, count):
	return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]
data = splitCount(line,50)
#print data
#output = ''
for d in data:
	#output = output + '00' + d
	iline = ''
	for i in d:
		if i is '1':
			iline = iline + '&&'
		else :
			iline = iline + '  '
	print iline
#print output
