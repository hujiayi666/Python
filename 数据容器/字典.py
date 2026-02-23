
mydict={"王力宏":{"语文":77,"数学":66,"英语":33},"周杰伦":{"语文":88,"数学":86,"英语":55},"林俊杰":{"语文":99,"数学":96,"英语":66}}
print(mydict)
mun1=mydict["王力宏"]
mun2=mydict["周杰伦"]
mun3=mydict["林俊杰"]
print(f"王力宏的语数外成绩为{mun1}")
print(f"周杰伦的语数外成绩为{mun2}")
print(f"林俊杰的语数外成绩为{mun3}")
mun1_1=mydict["王力宏"]["语文"]
mun2_1=mydict["周杰伦"]["语文"]
mun3_1=mydict["林俊杰"]["语文"]
print(f"王力宏的语文成绩为{mun1_1}分")
print(f"周杰伦的语文成绩为{mun2_1}分")
print(f"林俊杰的语文成绩为{mun3_1}分")
#增加元素
mydict["张兴哲"]={"语文":88,"数学":66,"英语":80}
print(f"增加元素后的字典为{mydict}")
#更新元素
mydict["王力宏"]={"语文":76,"数学":66,"英语":60}
print(f"更新元素后的字典为{mydict}")
#删除元素
score=mydict.pop("周杰伦")
print(f"字典中删除周杰伦分数后为{mydict},周杰伦的分数为{score}")
#清空元素
mydict.clear()
print(f"字典清空的结果：{mydict}")
#获取全部key
mydict={"王力宏":{"语文":77,"数学":66,"英语":33},"周杰伦":{"语文":88,"数学":86,"英语":55},"林俊杰":{"语文":99,"数学":96,"英语":66}}
keys=mydict.keys()
print(f"字典中的key有{keys}")
#通过for循环来遍历字典
for key in keys:
    print(f"字典的key是{key}")
    print(f"字典中的value是{mydict[key]}")
#直接for循环来遍历字典
for key in mydict:
    print(key)
    print(mydict[key])
#统计字典中的元素数量，len()
num=len(mydict)
print(f"字典中共有{num}个元素")





