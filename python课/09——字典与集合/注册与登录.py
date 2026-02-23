#创建一个字典，存放所有已注册用户的用户名和密码
dictionary={}   #创建一个空字典
users={}
#创建主菜单
def main():
    print("------------主菜单---------------")
    print("您好，这里是注册与登录系统，请选择操作:")
    print("注册信息，输入1")
    print("登录，输入2")
    print("退出，输入3")
    return int(input("请输入您的选择:"))
#注册函数
def register():
    for i in range (4):
        name=input("输入你要创建的用户名:")
        password=int(input("设置密码:"))
        dictionary[name]=password
        global users
        users=dictionary
#登录函数
def enroll():
    username = input("请输入用户名：")
    password = int(input("请输入密码："))
    if username not in users:
        print("用户名不正确！")
    elif users[username]!= password:
        print("密码不正确！")
    else:
        print("登录成功！")
#循环检查，输入数字调用函数
while True:
    key_input=main()
    if key_input==1:
        register()
        continue
    elif key_input==2:
        enroll()
        continue
    else:
        print("程序退出")
        break  #break函数阻断














