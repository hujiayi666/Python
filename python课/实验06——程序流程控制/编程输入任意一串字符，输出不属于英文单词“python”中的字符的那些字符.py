"""编程输入任意一串字符，输出不属于英文单词“python”中的字符的那些字符"""
# 首先，定义一个包含"python"的字符串
word = "python"
# 输入任意一串字符
input_string = input("请输入一串字符：")
# 创建一个空列表来存储不属于"python"的字符
result1 = []
# 遍历输入的字符串中的每个字符
for char in input_string:  #for循环
    # 如果字符不在"python"中，就将其添加到结果列表中
    if char not in word:
        result1.append(char)
# 输出结果
print("不属于'python'的字符是：", result1)

s = input("请输入一串字符：")
result = []
i = 0
while i < len(s):
    char = s[i]
    if char not in "python":
        result.append(char)
    i += 1
print("不属于'python'的字符是：",result)

