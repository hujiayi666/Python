import urllib.request

url="http://www.baidu.com"

response=urllib.request.urlopen(url)

#1个类型和6个方法
#print(type(response))#httpresponse类型

#按照一个一个字节读
#content=response.read()

#返回多少个字节
#content=response.read(6)

#读取一行
#content=response.readline()
#print(content)

#content=response.readlines()
#print(content)

#返回状态码
#print(response.getcode())

#返回url地址
#print(response.geturl())

#获取一个状态信息
print(response.getheaders())










