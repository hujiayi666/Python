money=5000000
name=None
#输入姓名
name=input("请输入您的姓名：")
#检查存款函数
def check(noshow):
    if noshow:
      print("------------查询余额--------------")
    print(f"{name},您好，您的余额为{money}员")
#存款函数
def saving(num):
    global money
    money+=num
    print("-------------存款---------------")
    print(f"{name},您好，您存款{num}员成功")
    check(False)
#取款函数
def get(num):
    global money
    money-=num
    print("-------------取款---------------")
    print(f"{name},您好，您取款{num}员成功,您的账号还剩{money}员")
    check(False)
#主菜单调用
def main():
    print("------------主菜单---------------")
    print(f"{name}您好，这里是ATM机，请选择操作:")
    print("查询余额，输入1")
    print("存款，输入2")
    print("取款，输入3")
    print("退出，输入4")
    return int(input("请输入您的选择:"))#retun返回输入
#循环检查，输入数字调用函数
while True:
    key_input=main()
    if key_input==1:
        check(True)
        continue
    elif key_input==2:
        num=int(input("您想要存多少钱，请输入："))
        saving(num)
        continue
    elif key_input==3:
        num=int(input("您想要取多少钱，请输入:"))
        get(num)
        continue
    else:
        print("程序退出")
        break#break函数阻断

