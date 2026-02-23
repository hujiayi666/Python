import re

s="ithema1 @@python2 !!!00999 #itcast"
result1=re.findall('\d',s)  #查数字
print(result1)

result2=re.findall('\W',s)   #查特殊字符
print(result2)

result3=re.findall('[a-zA-z]',s) #查字母
print(result3)

result4=re.findall('[0-9]',s)   #查数字
print(result4)


#匹配账号，只能由字母组成，且长度为6到10
r= '^[0-9a-zA-Z]{6,10}$'
s= '123456'
print(re.findall(r,s))

#匹配qq号，要求数字，长度在5到11位，第一位不为0
t='^[1-9][0-9]{4,10}$'
g='1785599'
print(re.findall(t,g))
#匹配邮箱地址
q='^[\w-]+(\.[\w-]+)*@(qq|163|gmail|outlook)(\.[\w-]+)+$'
a='1706373392@outlook.com'
print(re.findall(q,a))
print(re.match(q,a))



















