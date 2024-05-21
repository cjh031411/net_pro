from socket import *
import random

port=3333
BUFF_SIZE=1024

sock=socket(AF_INET,SOCK_DGRAM)
sock.connect(('localhost',port))

while True:
    msg=input('-> ')
    reTx=0
    while reTx<=5:
        resp=str(reTx)+' '+msg
        sock.send(resp.encode())
        sock.settimeout(2)

        try:
            data=sock.recv(BUFF_SIZE)
        except timeout:
            reTx+=1
            continue
        else:
            break

    sock.settimeout(None)
    while True:
        data=sock.recv(BUFF_SIZE)
        if random.random()<=0.5:
            continue
        else:
            sock.send(b'ack')
            print('<-',data.decode())
            break