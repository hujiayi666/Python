import random
num=random.randint(1,10)
guess=int(input("这是一个游戏，在1到10这十个数字中请输入你要猜的数字:"))
if int(guess)==num:
    print("恭喜你第一次就猜对了")
else:
    if int(guess)>num:
        print("你猜大了")
    else:
        print("你猜小了")
    guess=int(input("请再次输入你要猜的数字:"))
    if int(guess)==num:
        print("恭喜你第二次猜对了")
    else:
        if int(guess)>num:
            print("你猜大了")
        else:
            print("你猜小了")
        guess=int(input("请第三次输入你要猜的数字:"))
        if int(guess)==num:
            print("恭喜你第三次猜对了")
        else:
            print("很遗憾三次你都没猜到，正确答案是%s"%(num))























