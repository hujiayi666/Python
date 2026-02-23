# 从控制台输入 10 个数据并存放到列表中
data = []
i=0
for i in range(10):
    value = float(input(f"请输入第{str(i+1)}个数据："))
    data.append(value)
# 计算算术平均值
mean = sum(data) / len(data)
# 计算标准差
variance = sum((x - mean)**2 for x in data) / len(data)
std_dev=variance**(1/2)
# 计算中位数
sorted_data=sorted(data)
n = len(data)
if n % 2 == 1:                 #如果n是奇数，则序列的最中间位置是一个数据，可以表示为sn//2
    median = sorted_data[n // 2]
else:                          #如果n是偶数，序列不存在一个最中间位置，则中位数表示为最中间两个位置数据的平均值
    mid1 = sorted_data[n // 2 - 1]
    mid2 = sorted_data[n // 2]
    median = (mid1 + mid2) / 2
# 输出结果
print(f"列表为{data}")
print(f"算术平均值为：{mean}")
print(f"标准差为：{std_dev}")
print(f"中位数为：{median}")











