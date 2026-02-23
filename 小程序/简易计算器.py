#加法运算
def add():
    x=int(input("输入自变量："))
    y=int(input("输入应变量："))
    result=x+y
    print(f"{x}+{y}的值为{result}")
#减法运算
def jian():
    x=int(input("输入自变量："))
    y=int(input("输入应变量："))
    result=x-y
    print(f"{x}-{y}的值为{result}")
#乘法运算
def cheng():
    x=int(input("输入自变量："))
    y=int(input("输入应变量："))
    result=x*y
    print(f"{x}*{y}的值为{result}")
#除法运算
def chu():
    x=int(input("输入自变量："))
    y=int(input("输入应变量："))
    result=x/y
    print(f"{x}/{y}的值为{result}")
#调用函数
def main():
    print("欢迎使用计算器")
    print("加法请按1")
    print("减法请按2")
    print("乘法请按3")
    print("除法请按4")
    return int(input("请输入你的选择："))
while True:
    key_input=main()
    if key_input==1:
        add()
        continue
    elif key_input==2:
        jian()
        continue
    elif key_input==3:
        cheng()
        continue
    elif key_input==4:
        chu()
    else:
        print("程序退出")
        break










