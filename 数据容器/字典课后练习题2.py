mydict={"王力宏":{"部门":"科技部","工资":3000,"级别":1},
        "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
        "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
        "张学友":{"部门":"科技部","工资":4000,"级别":1},
        "刘德华":{"部门":"市场部","工资":6000,"级别":2}}
print(f"升级前员工级别：{mydict}")
#用for循环从原字典中调取value
for wage in mydict:
#用if语句来判断工资是否大于5000
    if mydict[wage]["工资"]>=5000:
#定义一个新字典来接受从原字典中调取的元素
        newmydict=mydict[wage]
#把符合条件的员工级别加1
        newmydict["级别"]+=1
#将改变后的字典返回给原字典
        mydict[wage]=newmydict
#运用else语句来调取低于5000员的员工
    else:
#用新字典接受调取的员工信息
        newmydict = mydict[wage]
#将符合条件员工的等级加2
        newmydict["级别"]+=2
#将改变后的结果返回给原字典
        mydict[wage]=newmydict
print(f"升级后员工级别：{mydict}")






