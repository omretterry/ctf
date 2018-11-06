from PIL import Image

f=Image.open('not_art.png')
f=f.convert('RGB')
print f.getcolors()
pix = f.load()

#colorList = []
#for x in range(5,300,10):
# 	for y in range(5,300,10):
		#print (x,y)
		#print f.getpixel((x, y))
#		print pix[x,y]
		#if pix[x,y] not in colorList:
		#	colorList.append(pix[x,y])	
#for i in colorList:
#	print ii

#print pix[.5,.5]
#print pix[1.5,.5]

start = 5
end = 295
index = 15

output = ''

for x in range(start,end,10):
	print pix[x,start]
	if pix[x,start][2] != 255:
		output = output + '0'
	else:
		output += '1'

for i in range(1,8):
	for y in range(start,end,10):
		print pix[end,y]
		if pix[end,y][2] != 255:
			output += '0'
		else:
			output += '1'
			
	for x in range(end,start,-10):
		print pix[x,end]
                if pix[x,end][2] != 255:
                        output += '0'
                else:
                        output += '1'


	for y in range(end,start+20,-10):
		print pix[start,y]
                if pix[start,y][2] != 255:
                        output += '0'
                else:
                        output += '1'


	for x in range(start,end-20,10):
		print pix[x,start]
                if pix[x,start][2] != 255:
                        output += '0'
                else:
                        output += '1'


	start = start + 20
	end = end - 20

print output
