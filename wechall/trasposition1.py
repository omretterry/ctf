text =  '''oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wg miaffifdhg.m'''
newtext = ''
i=0
while i<len(text)-1:
	newtext += text[i+1]
	newtext += text[i]
	i += 2
print newtext