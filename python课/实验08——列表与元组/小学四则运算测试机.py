"""系统随机产生[ 1,10 ]之间的两个操作数，随机产生一个运算符 ( +, -, *, / )， 把操作数和运算符作为一个算式题目显示给用户看，用户输入算式的运算结果。
程序判断是否正确，并给出提示如“您答对了”或“您算错了”。不管是否答对，同一道题，只答一次。
让用户不停地答题，直到他输入’10000’，退出答题。"""
import random
while True:
    a=random.randrange(0,11)
    b=random.randrange(0,11)
    operators = ["+", "-", "*", "/"]
    operator=random.choice(operators)
    question=f"{a}{operator}{b}="
    result=eval(f"{a}{operator}{b}")
    answear=float(input(question))
    if answear==10000:
        print("程序退出")
        break
    elif answear==result:
        print("您答对了")
    else:
        print("您算错了")









