#导包
import requests
from lxml import etree


#发送给谁
url="https://xiyouji.5000yan.com/19830.html"
#伪装自己
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"}

#发送请求
response=requests.get(url,headers=headers)
#设置编码
response.encoding="UTF-8"
#响应信息
print(response.text)
e=etree.HTML(response.text)







#保存


















