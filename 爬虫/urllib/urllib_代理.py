import urllib.request
url="https://www.baidu.com/s?wd=ip"

headers={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
#请求对象的定制
requests=urllib.request.Request(url=url,headers=headers)
#模拟浏览器访问服务器
#response=urllib.request.urlopen(requests)
proxies={"http":"218.87.205.93:20133"}


handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(requests)
content=response.read().decode("UTF-8")

#保存
f=open("../daili.html", "w", encoding="UTF-8")
f.write(content)
f.close()
































