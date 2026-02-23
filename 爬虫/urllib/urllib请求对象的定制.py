import urllib.request

url="http://www.baidu.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
#因为urlopen方法不能存储字典，所以headers不能传递出去
#注意，因为参数顺序的问题，不能直接写url和headers,中间还有data，所以要关键字传参
request=urllib.request.Request(url=url,headers=headers)
respones=urllib.request.urlopen(request)

content=respones.read().decode("UTF-8")
print(content)



























