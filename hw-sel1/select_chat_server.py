import socket
import time
import threading
import select

BUFSIZE=1024

socks=[]

s_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_sock.bind(('',2500))
s_sock.listen(5)

socks.append(s_sock)

print('Server Started')

while True:
    r_sock,w_sock,e_sock=select.select(socks,[],[])

    for s in r_sock:
        if s==s_sock:
            c_sock,addr=s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            data=s.recv(BUFSIZE)
            if 'quit' in data.decode():
                if s in socks:
                    print(addr,'exited')
                    socks.remove(s)
                    continue
            
            print(time.asctime() + str(addr) + ':' + data.decode())

            for client_sock in socks:
                if client_sock != s and client_sock!=s_sock:
                    client_sock.send(data)

