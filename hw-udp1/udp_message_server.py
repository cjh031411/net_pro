from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

mbox=[0]

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    recv_msg=data.decode()
    l=recv_msg.split()

    for i in range(3,len(l)):
        l[2]=l[2]+' '+l[i]
    
    
    
    ID=int(l[1])
    if l[0]=='send':
        final_list=[]
        for i in range(3):
            final_list.append(l[i])
        print(final_list)
        resp='OK'
        if ID not in mbox:
            mbox.append([])
            mbox[ID].append(final_list[2])
    elif l[0]=='receive':
        if not mbox[ID]:
            resp='No messages'
            sock.sendto(resp.encode(), addr)
            continue
        resp=mbox[ID][0]
        del mbox[ID][0]

    elif l[0]=='quit':
        addr.close()
    
    sock.sendto(resp.encode(), addr)