#urlencode的应用场景：多个参数的时候

#https://www.baidu.com/s?wd=周杰伦&sex=男
#获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE
import urllib.parse
import urllib.request
base_url="https://www.baidu.com/s?"
data={
    "wd":"周杰伦",
    "sex":"男",
    "location":"中国台湾"
}
new_url=urllib.parse.urlencode(data)
url=base_url+new_url
#反爬
headers={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
request=urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
respones=urllib.request.urlopen(request)
#获取响应的内容
content=respones.read().decode("UTF-8")

print(content)













