word='led=on&motor=off&switch=off'

d=dict()
tmp=str()
l=[]

for i in word:
    if i=='=' or i=='&':
        l.append(tmp)
        tmp=''
    else:
        tmp+=i
    
l.append(tmp)
print(l)

for i in range(len(l)//2):
    d[l[i*2]]=l[i*2+1]

print(d)