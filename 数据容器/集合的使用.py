A1={1,3,6,8,10,100,10,1,2,3,4,5,6,8}
A1.add(11)#集合的添加
print(f"A1集合添加元素后的结果是{A1}")

A1.remove(10)#集合的移除
print(f"A1集合移除元素后的结果是{A1}")

eletment=A1.pop()#集合的取出
print(f"集合取出的元素是{eletment},取出元素后集合是{A1}")

A1.clear()#集合的清除
print(f"集合清空后的结果是{A1}")
#差集的使用
set1={1,7,8}
set2={1,3,4}
set3=set1.difference(set2)
print(f"集合1中有而集合2中没有的元素组成的集合是{set3}")
#消除差集的方法
set1={1,3,5,7,9}
set2={1,2,4,6,7,8}
set1.difference_update(set2)
print(set1)
#合并集合的方法
set1={1,3,5,7,9}
set2={1,2,4,6,8,10}
set3=set1.union(set2)
print(f"集合1与集合2的并集合为{set3}")
#统计集合中的元素数量
set1={1,2,3,4,5,6,7,8,9,10}
i=len(set1)
print(f"集合1中共有{i}个元素")
#集合的遍历
set1={1,2,3,4,5,6,7,8,9,10}
for i in set1:
    print(f"集合1的元素有:{i}")
#列表转集合
mylist=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
myset=set()
for i in mylist:
    myset.add(i)
print(mylist)
print(f"有列表：{myset}")