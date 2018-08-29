import re
from socket import *


# func: get output str of numbers between inv
def getInv(inv):
    invList = []
    split = ' '
    for i in range(inv[0], inv[1]):
        invList.append(str(i))        
    return split.join(invList)

# server addr info
HOST = 'pwnable.kr'  # local at pwnable.kr
PORT = 9007
ADDR = (HOST, PORT)
BUFSIZE = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

# start: [Server]: N=? C=?
startPattern = re.compile(r'^N=(\d*)\sC=(\d*)$');
# step: [Server]: ***0 (qual)
qualPattern = re.compile(r'^(\d*0)$');
# step: [Server]: ***9 (unqual)
unqualPattern = re.compile(r'^(\d*9)$');

curInv = None  # current interval
preInv = None  # previous interval

while True:
    data = clientSocket.recv(BUFSIZE)
    print data

    match1 = startPattern.match(data)  
    match2 = qualPattern.match(data)  
    match3 = unqualPattern.match(data)  

    if match1:  # match startPattern
        curInv = (0, int(match1.group(1))/2) 
        preInv = (0, int(match1.group(1))) 
        print getInv(curInv)
        clientSocket.send(getInv(curInv) + '\r\n')  # send numbers to HOST 

    elif match2:  # match qualPattern
        preInv = (curInv[1], preInv[1])
        curInv = (preInv[0], (preInv[0]+preInv[1])/2 + (preInv[0]+preInv[1])%2)
        print getInv(curInv)
        clientSocket.send(getInv(curInv) + '\r\n')

    elif match3:  # match unqualPattern
        preInv = curInv
        curInv = (preInv[0],  (preInv[0]+preInv[1])/2 + (preInv[0]+preInv[1])%2)
        print getInv(curInv)
        clientSocket.send(getInv(curInv) + '\r\n')

    elif 'wrong' in data or 'error' in data or 'bye' in data:
        break

clientSocket.close()
