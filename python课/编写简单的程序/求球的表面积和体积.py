"""编写程序，从键盘上输入球的半径，计算输出球的表面积和体积，要求输入和输出的数字结果之前都具有一定的文字提示"""
import math
r=eval(input("请输入球的半径:"))
space=4*math.pi*r**2
volume=(4/3)*math.pi*r*r*r
print(f"球的表面积为{space},体积为{volume}")






