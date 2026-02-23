import random
num=random.randint(1,100)
flag=True
count=0
while flag:
    guess=int(input("请输入你要猜的数字："))
    count +=1
    if guess==num:
        print("恭喜你猜对了")
        flag=False
    else:
        if guess>num:
            print("你猜大了")
        else:
            print("你猜小了")
print(f"你总共猜了{count}次")















