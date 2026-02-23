"""编程输入任意一串字符，分别统计其中英文字母和数字的个数"""
s = input("请输入一串字符：")
letter_count = 0
digit_count = 0
for char in s:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print(f"输入的字符串中英文字母的个数为：{letter_count}")
print(f"输入的字符串中数字的个数为：{digit_count}")