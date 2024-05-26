import socket
import time
import threading

BUFSIZE=1024

def recv_task(sock,addr):
    global client
    while True:
        data=sock.recv(BUFSIZE)
        if 'quit' in data.decode():
            if addr in clients:
                print(addr,'exited')
                clients.remove((sock,addr))
                sock.close()
                break
                
          
        if (sock,addr) not in clients:
            print('new client',addr)
            clients.append((sock,addr))
        print(time.asctime()+str(addr)+':'+data.decode())
        for client_sock,client_addr in clients:
            if client_sock != sock:
                client_sock.send(data)

clients=[]
clients_socket=[]

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',2500))
s.listen(5)

print('Server Started')

while True:
    conn,addr=s.accept()
    
    th=threading.Thread(target=recv_task,args=(conn,addr))
    clients_socket.append(th)
    th.start()

