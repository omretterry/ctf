from PIL import Image

img = Image.open('diff.png')
print img.size
pix = img.load()
line = ''
#for y in range(img.size[1]):
#	line = ''
#	for x in range(img.size[0]):
#		line = line + str(pix[x,y])
#	print line 
for y in range(img.size[1]):
	line = line + str(pix[0,y])
print line
''' 
def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

morse = ''
data = splitCount(line,2)
print data
for i in data:
	if i == "01":
		morse = morse + '.'
	elif i == "00":
		morse = morse + ' '
	elif i == "11":
		morse = morse + '_'
print morse
'''
