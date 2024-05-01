import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',3333))
s.listen(5)

while True:
    client,addr=s.accept()
    print('connection from ',addr)
    while True:
        cal=(client.recv(1024)).decode()
        if not cal:
            break
        cal_list=cal.split()
        num1=int(cal_list[0])
        operator=cal_list[1]
        num2=int(cal_list[2])

        if(operator=='+'):
            result=num1+num2
        elif(operator=='-'):
            result=num1-num2
        elif(operator=='*'):
            result=num1*num2
        elif(operator=='/'):
            result=num1/num2
        msg=(str(result)).encode()
        client.send(msg)

    client.close()