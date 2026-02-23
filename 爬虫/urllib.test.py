#使用urllib获取百度首页的源码
import requests
import urllib.request
#(1)定义一个url
url="http://www.baidu.com"
#(2)模拟浏览器向服务器发送请求
res=urllib.request.urlopen(url)

#(3)获取响应中的页面源码
#解码——————encode
content=res.read().decode("UTF-8")

#打印数据
print(content)








































