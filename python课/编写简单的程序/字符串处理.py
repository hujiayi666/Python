s = "http://sports.sina.com.cn/"
# 1. 字符串中字母 t 出现的次数
t_count = s.count('t')
print(f"字母 t 出现的次数为：{t_count}")
# 2. 字符串中"com”子字符串出现的位置
com_pos = s.find('com')
print(f"子字符串 'com' 出现的位置为：{com_pos}")
# 3. 将字符串中所有的".替换为"_"
new_s = s.replace('.', '_')
print(f"替换后的字符串为：{new_s}")
# 4. 提取"sports"和"sina”两个子字符串(分别使用正向切片和反向切片方式)
sports_pos = s.find('sports')
sina_pos = s.find('sina')
sports = s[sports_pos:sports_pos+6]
sina_reverse = s[-3:-7:-1][::-1]
print(f"正向切片提取的'sports'为：{sports}")
print(f"反向切片提取的'sina'为：{sina_reverse}")
# 5. 将字符串中的字母全变为大写
upper_s = s.upper()
print(f"变为大写后的字符串为：{upper_s}")
# 6. 输出字符串的总字符个数。在字符串后拼接子字符串"index"
length = len(s)
new_str = s + "index"
print(f"字符串总字符个数为：{length}")
print(f"拼接后的字符串为：{new_str}")