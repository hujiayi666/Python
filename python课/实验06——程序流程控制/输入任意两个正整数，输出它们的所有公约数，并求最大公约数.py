"""输入任意两个正整数，输出它们的所有公约数，并求最大公约数"""
a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))
common_divisors = []
gcd = 1
# 求公约数并找出最大公约数
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        common_divisors.append(i)
        gcd = i
print(f"{a}和{b}的公约数有：{common_divisors}")
print(f"{a}和{b}的最大公约数是：{gcd}")

