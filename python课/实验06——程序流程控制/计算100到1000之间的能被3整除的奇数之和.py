"""计算100到1000之间的能被3整除的奇数之和"""
#while循环
sum_result = 0
num =101
while num < 1001:
    if num % 3 == 0:
        sum_result += num
    num += 2
print(f"100到1000之间的能被3整除的奇数之和为{sum_result}")

#for循环
sum_result1=0
for i in range(101,1001,2):
    if i %3==0:
        sum_result1 +=i
print(f"100到1000之间的能被3整除的奇数之和为{sum_result1}")