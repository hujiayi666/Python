# 首先，定义一个包含"python"的字符串
word = "python"
# 输入任意一串字符
input_string = input("请输入一串字符：")
# 创建一个空列表来存储不属于"python"的字符
result = []
# 遍历输入的字符串中的每个字符
for char in input_string:
    # 如果字符不在"python"中，就将其添加到结果列表中
    if char not in word:
        result.append(char)
# 输出结果
print("不属于'python'的字符是：", result)