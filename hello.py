a,b=map(int,input().split())

if(a<b):
    tmp=a
    a=b
    b=tmp

while b!=0:
    n=a%b
    a=b
    b=n

print(a)