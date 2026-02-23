#使用场景：数据采集时，需要绕过登录，然后进入到某个页面
#什么情况下访问不成功？
#因为请求头的信息不够，所以访问不成功
import urllib.request
url="https://weibo.cn/msg/?tf=5_010"
headers={"Cookie":
"SCF=AvQh0oPbCM7OcrninMcu_UC_4UcQ9JkQolfscogtygCOoBAKZ5USE-eMLtgUzICkUzVDiYWRrq2RuQgefn54P0Q.; SUB=_2A25LJhVnDeRhGeFG71cQ8CjOzzWIHXVoWiivrDV6PUJbktAGLUjikW1NeWNcXkD8DH9748Y1mZ1Iach72hWLikCE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh73y4Js3OI6fP4TSuQ8Lco5NHD95QN1hBfeK5ceoB4Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0nXSK27SozX1Btt; SSOLoginState=1713530167; ALF=1716122167; _T_WM=a61578dc0fee2bc362cea0bb53684d99; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000173; _TTT_USER_CONFIG_H5=%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D",
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

requests=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(requests)

content=response.read().decode("UTF-8")

f=open("weibo.html","w",encoding="UTF-8")
f.write(content)
f.close()