import re
s="1python itheima itcast python"
result=re.search("python",s)
print(result)
print(result.group())
print(result.span())

result1=re.findall("python",s)
print(result1)

result2=re.match("python",s)
print(result2)
print(result2.group())
print(result2.span())








