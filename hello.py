d= [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone':'555-3141', 'email':''},
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

#전화번호가 8로 끝나는 사용자 이름을 출력하라
for i in d:
    if i['phone'][-1]=='8':
        print(i['name'],end=' ')
print()

#이메일이 없는 사용자 이름을 출력하라
for i in d:
    if i['email']=='':
        print(i['name'],end=' ')
print()

#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
inp_name=input()
    
found=False
for i in d:
    if inp_name==i['name']:
        print(i['phone'],i['email'])
        found=True
if found==False:
    print("이름이 없습니다")