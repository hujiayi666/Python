import os


def get_html(month, day):
    # 确保目录存在
    os.makedirs('htmls', exist_ok=True)

    # 创建或打开文件
    html_file = open('htmls/%d%d.html' % (month, day), 'w', encoding='UTF-8')
    # 写入数据或进行其他操作
    html_file.close()
