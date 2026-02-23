#在 [1, 100] 之间产生两个随机整数a、b，输出a、b两数的最大公约数和最小公倍数。
import random
#随机生成两个数
a=random.randint(1,100)
b=random.randint(1,100)
# 求公约数并找出最大公约数
common_divisors = []
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        common_divisors.append(i)
        gcd = i
# 求最小公倍数
lcm= a * b // gcd
#打印结果
print(f"随机生成的两个数为 {a} 和 {b}。")
print(f"{a}和{b}的最大公约数是：{gcd}")
print(f"它们的最小公倍数是 {lcm}。")