money=10000
import random
for i in range(1,21):
    num=random.randint(1,10)
    if num<5:
        print(f"员工{i},绩效分{num},低于5，不发工资，下一位。")
        continue
    if money>=1000:
        money-=1000
        print(f"员工{i},绩效分{num},发工资1000员,公司余额：{money}")
    else:
        print(f"员工{i},余额不足，当前余额:{money},不足以发工资，请下个月再来。")
        break





