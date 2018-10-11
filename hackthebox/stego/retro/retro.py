f = open('output')
message = ''
for line in f.readlines():
	#print len(line)
	if len(line) > 20:
		message = message + "1"
	else:
		message = message + "0"
print message
