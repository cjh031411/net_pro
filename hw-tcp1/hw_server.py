import socket

s=socket.socket(socket.AF_INET,
                socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client,addr=s.accept()
    print('Connection from',addr)
    client.send(b'hello ' + addr[0].encode())
    msg=client.recv(1024)
    print(msg.decode())
    a=20191593 
    b=a.to_bytes(4,'big')
    client.send(b)
    client.close()