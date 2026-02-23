import requests
from bs4 import BeautifulSoup
import csv

# 发送HTTP请求获取网页内容
url = "http://m.toutiao.com/group/7326182115065102888/?upstream_biz=doubao"
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到包含GDP数据的表格
table = soup.find('table')

# 提取表格的表头和数据行
headers = [th.text.strip() for th in table.find('tr').find_all('th')]
rows = table.find_all('tr')[1:]

# 存储数据的列表
data = []

# 遍历数据行，提取并整理数据
for row in rows:
    cols = row.find_all('td')
    row_data = [col.text.strip() for col in cols]
    data.append(row_data)

# 将数据写入CSV文件
with open('2023_provinces_gdp.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(headers)
    # 写入数据行
    writer.writerows(data)