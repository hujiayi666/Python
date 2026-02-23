#输入一句英文句子，输出其中长度最长的单词。（注意可以用split( )方法将英文句子分离出单词，存放至列表处理）
sentence = input("请输入一句英文句子：")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"长度最长的单词是：{longest_word}")