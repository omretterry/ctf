import os

output = [''] * 50
print output
dirlist = os.walk('secret')
for root,dirs,files in dirlist:
	print(root,files)

	for fileitem in files:
		#pass
		if len(root.split('/')) > 0:
			print (int(fileitem),output[int(fileitem)])
			output[int(fileitem)] = root.split('/')[1]
print "".join(output)
