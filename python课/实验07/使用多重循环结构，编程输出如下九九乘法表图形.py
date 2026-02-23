"""使用多重循环结构，编程输出如下九九乘法表图形"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end="")
    print()