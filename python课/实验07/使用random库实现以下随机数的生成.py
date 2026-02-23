#使用random库实现以下随机数的生成
import random
# （1）随机生成一个[1,6]间的整数。
random_int_1_to_6 = random.randint(1, 6)
print(f"随机生成一个[1,6]间的整数为：{random_int_1_to_6}")
# （2）随机生成一个[60,100)之间的浮点数。
random_float_60_to_100 = random.uniform(60, 100)
print(f"随机生成一个[60,100)之间的浮点数为{random_float_60_to_100}")
# （3）随机生成一个 0 到 100 间的 3 的倍数。
random_multiple_of_3 = random.randrange(0, 101, 3)
print(f"随机生成一个 0 到 100 间的 3 的倍数为{random_multiple_of_3}")