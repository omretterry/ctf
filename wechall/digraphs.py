text = 'xyctgmfsyihsyaxbushsyaclctgmpegg ujctxb aecuswyiytxkyacuae yacvclpe rzcupepehsfscu pexbswswcupepekvxbususytgg rhhspe gmctya yactct aeclkvkvclswxbusya cuclyacvcuyioj bzhspe clyavj rhcuususoj fsctctae dectdngg ktgmyacuyi yacvclpe hkcuytbzctyiae hspe pectusxbyaclctgmzn dncuclfskvcvxkususpecuswgg'
text = text.split()

codemap = [
    ['hs','a'],
    ['xy','c'],
    ['sw','c'],
    ['ae','d'],
    ['cu','e'],
    ['kv','f'],
    ['fs','g'],
    ['cv','h'],
    ['cl','i'],
    ['sh','k'],
    ['us','l'],
    ['rz','m'],
    ['gm','n'],
    ['ct','o'],
    ['xk','p'],
    ['yi','r'],
    ['pe','s'],
    ['ya','t'],
    ['xb','u'],
    ['ub','w'],
    ['pw','y'],
    ['yt','y'],
    ['uj','y'],
    ['gg','!'],
]

for i in text:
    newtext = ''
    if i != ' ':
        j = 0
        while j < len(i)-1:
            pairkey = i[j] + i[j+1]
            if any(pairkey in keycode for keycode in codemap):
                for keycode in codemap:
                    if i[j] + i[j+1] == keycode[0]:
                        newtext += keycode[1] 
            else:
                newtext += '*'
            j += 2
    else:
        newtext += ' '
    print newtext