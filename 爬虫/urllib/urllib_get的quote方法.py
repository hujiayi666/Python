import urllib.request
import urllib.parse
url="https://www.baidu.com/s?wd="
#请求定制为了解决反爬的第一种手段
header={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
#将周杰伦三个自用unicode编码格式
name=urllib.parse.quote("周逸")
url=url+name
request=urllib.request.Request(url=url,headers=header)
#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)

#获取响应的内容
content=response.read().decode("UTF-8")

print(content)

























