from socket import *

s=socket()
s.bind(('127.0.0.1',80))
s.listen(10)

while True:
    c,addr=s.accept()

    data=c.recv(1024)
    msg=data.decode()
    req=msg.split('\r\n')
    
    filename=req[0].split()[1][1:]

    ok=True

    if(filename=='index.html'):
        f=open(filename,'r',encoding='utf-8')
        mimeType='text/html'
        ok=True
    elif(filename=='favicon.ico'):
        f=open(filename,'rb')
        mimeType='image/x-icon'
        ok=True
    elif(filename=='iot.png'):
        f=open(filename,'rb')
        mimeType='image/png'
        ok=True
    else:
        ok=False

    if(ok==True):
        c.send(('HTTP/1.1 200 OK\r\n'
               'Content-Type: ' + mimeType + '\r\n'
               '\r\n').encode())
        data=f.read()
        if(filename=='index.html'):
            c.send(data.encode('euc-kr'))
        if(filename=='favicon.ico'):
            c.send(data)
        if(filename=='iot.png'):
            c.send(data)    
    elif(ok==False):
        c.send(('HTTP/1.1 404 Not Found\r\n'
               '\r\n'
               '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
               '<BODY>Not Found</BODY></HTML>').encode())
    c.close()


    


    #웹서버 코드
    #각 객체 전송 후 소켓 닫기