from random import randint

money=50

while True:
    coin=randint(1,2)
    predict=randint(1,2)
    if(predict==coin):
        money+=9
    else:
        money-=10
    print(money,"$")


    if(money<=0):
        print("you lose")
        break
    elif(money>=100):
        print("you win")
        break