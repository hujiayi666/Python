#https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20
#https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=20&limit=20
#https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=40&limit=20


#下载豆瓣电影前10页的数据
#(1)请求对象定制
#（2）获取响应的数据
#（3）下载数据
import urllib.parse
import urllib.request
def creat_request(page):
    base_url="https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&"
    data={"start":(page-1)*20,
          "limit":20}
    data=urllib.parse.urlencode(data)
    url=base_url+data
    headers={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    request=urllib.request.Request(url=url,headers=headers)
    return request


def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode("UTF-8")
    return content
def download(page,content):
    f=open("douban"+str(page)+".json","w",encoding="UTF-8")
    f.write(content)
    f.close()
if __name__=="__main__":
    start_page=int(input("起始页码:"))
    end_page=int(input("结束页码:"))

    for page in range(start_page,end_page+1):
#       每一页都有自己的请求对象的定制
        request=creat_request(page)
        #获取响应数据
        content=get_content(request)
        #下载
        download(page,content)


