import urllib.request


proxies_pool=[{"http":"218.87.205.93:20133"},
              {"http":"65.109.203.176:80"},
              {"http":"212.102.34.54:8443"},
              {"http":"202.101.213.251:19127"}
              ]
import random

proxies=random.choice(proxies_pool)




url="https://www.baidu.com/s?wd=ip"
headers={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

requests=urllib.request.Request(url=url,headers=headers)

handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)

response=opener.open(requests)

content=response.read().decode("UTF-8")

with open("dailis.html","w",encoding="UTF-8")as f:
    f.write(content)








