"""用整数0～6依次表示星期日、星期一、星期二、……、星期六，编程实现如下功能：
输入一个整数，输出其对应的是星期几。
如果输入的整数不在0～6之内，则显示“输入数据错误”。"""
a=int(input("输入一个整数:"))
if a==0:
    print("星期一")
elif a==1:
    print("星期二")
elif a==2:
    print("星期三")
elif a==3:
    print("星期四")
elif a==4:
    print("星期五")
elif a==5:
    print("星期六")
elif a==6:
    print("星期天")
else:
    print("输入数据错误")