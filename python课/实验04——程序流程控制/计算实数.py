"""编程实现如下功能：输入任意一个实数X , 根据下列公式求y的值并输出。"""
x=float(input("输入一个实数:"))
if x>20:
    y=x-20
    print(y)
elif 0<x<=20:
    y=(x+5)**0.5
    print(y)
else:
    y=100-x**2
    print(y)