"""编程求解一元二次方程Ax2+Bx+C=0。输入的方程的系数A、B、C，要求区分A、B、C的各种可能取值，求解相应的方程，并输出结果"""
import math
A = float(input("请输入方程系数 A："))
B = float(input("请输入方程系数 B："))
C = float(input("请输入方程系数 C："))
if A == 0:
    if B == 0:
        if C == 0:
            print("方程有无穷多解。")
        else:
            print("方程无解。")
    else:
        x = -C / B
        print(f"方程为一元一次方程，解为 x = {x}。")
else:
    discriminant = B**2 - 4*A*C
    if discriminant > 0:
        x1 = (-B + math.sqrt(discriminant)) / (2*A)
        x2 = (-B - math.sqrt(discriminant)) / (2*A)
        print(f"方程有两个不同的解：x1 = {x1}, x2 = {x2}。")
    elif discriminant == 0:
        x = -B / (2*A)
        print(f"方程有两个相同的解：x = {x}。")
    else:
        real_part = -B / (2*A)
        imaginary_part = math.sqrt(-discriminant) / (2*A)
        print(f"方程有两个共轭复根：x1 = {real_part}+{imaginary_part}i, x2 = {real_part}-{imaginary_part}i。")