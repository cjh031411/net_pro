days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30,
        'December':31}

#사용자가 월을 입력하면 해당 월에 일수를 출력하라
month=input()
print(days[month])

#알파벳 순서로 모든 월을 출력하라.
month_list=list(days.keys())
month_list.sort()
print(month_list)

#일수가 31인 월을 모두 출력하라
day31_list=[]
for i in days.keys():
    if days[i]==31:
        day31_list.append(i)
print(day31_list)

#월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
sorted_days=sorted(days.items(),key=lambda item:item[1])
print(sorted_days)

#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
word=input()
for i in days.keys():
    if word in i:
        print(days[i])