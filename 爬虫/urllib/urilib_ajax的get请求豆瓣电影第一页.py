#get请求
#获取豆瓣电影第一页的数据
import urllib.request

url="https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20"
headers={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)

#获取响应数据
response=urllib.request.urlopen(request)
content=response.read().decode("UTF-8")

#数据下载到本地
fp=open("../douban.json", "w", encoding="UTF-8")
fp.write(content)































