import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# 读取文本文件内容
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 去除各种可能导致问题的特殊字符和多余空白等
    text = re.sub(r'\s+','', text)  # 将连续的空白字符替换为单个空格
    text = re.sub(r'[^\w\s]','', text)  # 去除除了字母、数字、汉字和空格之外的字符

    return text

# 对文本进行分词并统计词频
def word_frequency_count(text):
    words = jieba.cut(text)
    word_count = Counter(words)
    return word_count


# 绘制词云图
def draw_word_cloud(word_count):
    # 将词频数据转换为字典格式，键为单词，值为频率
    frequencies_dict = dict(word_count)

    wordcloud = WordCloud(font_path='simhei.ttf',  # 设置中文字体路径，确保能正确显示中文
                          width=800,
                          height=600,
                          background_color='white')

    wordcloud.generate_from_frequencies(frequencies_dict)

    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    file_path = "C:\\python\\实验12资料\\三国演义.txt"
    text = read_text_file(file_path)
    word_count = word_frequency_count(text)
    draw_word_cloud(word_count)