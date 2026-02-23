import urllib.request
import urllib.parse
def creat_request(page):
    base_url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data={"cname": "北京",
"pid":"",
"pageIndex":page,
"pageSize": "10"}
    data=urllib.parse.urlencode(data).encode("UTF-8")
    headers={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    request=urllib.request.Request(url=base_url,headers=headers,data=data)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode("UTF-8")
    return content
def download(page,content):
    f=open("kfc"+str(page)+".json","w",encoding="UTF-8")
    f.write(content)
    f.close()
if __name__ =="__main__":
    start_page = int(input("起始页码:"))
    end_page = int(input("结束页码:"))
    for page in range(start_page, end_page + 1):
        #       每一页都有自己的请求对象的定制
        request = creat_request(page)
        # 获取响应数据
        content = get_content(request)
        # 下载
        download(page, content)









































