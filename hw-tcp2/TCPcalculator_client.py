import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',3333))

while True:
    cal=input("계산식 입력:")
    if(cal=='q'):
        break
    msg=cal.encode()
    s.send(msg)
    result=float((s.recv(1024)).decode())
    print("계산결과는 : {:.1f}".format(result))
        



s.close()