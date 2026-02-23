#创建空字典dic_student
dic_student = {}
#由用户依次输入五名学生的姓名和年龄，存入字典dic_student
for i in range(5):
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    dic_student[name] = age
#输出字典dic_student中的内容（注意，年龄数字是对齐的）
for name, age in dic_student.items():
    print(f"{name:<8}{age:>2d}")
#打印五名学生的最大年龄、最小年龄和平均年龄
ages = list(dic_student.values())
max_age = max(ages)
min_age = min(ages)
average_age = sum(ages) / len(ages)
print(f"最大年龄：{max_age}")
print(f"最小年龄：{min_age}")
print(f"平均年龄：{average_age}")










