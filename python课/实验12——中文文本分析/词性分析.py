import jieba.posseg as pseg
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 读取文本文件内容
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


# 对文本进行分词并按词性统计词频
def word_frequency_count_by_pos(text):
    noun_count = Counter()
    verb_count = Counter()
    adj_count = Counter()

    words = pseg.cut(text)
    for word, flag in words:
        if flag.startswith('n'):  # 名词
            noun_count[word] += 1
        elif flag.startswith('v'):  # 动词
            verb_count[word] += 1
        elif flag.startswith('a'):  # 形容词
            adj_count[word] += 1

    return noun_count, verb_count, adj_count


# 绘制词云图
def draw_word_cloud(word_count, title):
    frequencies_dict = dict(word_count)

    wordcloud = WordCloud(font_path='simhei.ttf',  # 设置中文字体路径，确保能正确显示中文
                          width=800,
                          height=600,
                          background_color='white')

    wordcloud.generate_from_frequencies(frequencies_dict)

    plt.figure(figsize=(10, 8))
    plt.title(title)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    file_path = "C:\\python\\实验12资料\\三国演义.txt"
    text = read_text_file(file_path)

    noun_count, verb_count, adj_count = word_frequency_count_by_pos(text)

    draw_word_cloud(noun_count, "《三国演义》名词词频词云图")
    draw_word_cloud(verb_count, "《三国演义》动词词频词云图")
    draw_word_cloud(adj_count, "《三国演义》形容词词频词云图")