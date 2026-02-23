#设计一个类
class Student:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add
#for循环录入信息
for i in range (10):
    print(f"当前录入第{i+1}位学生信息，总共需要录入10位学生信息。")
    stu = Student(input("请输入学生姓名："),
                  input("请输入学生年龄："),
                  input("请输入学生地址:"))
    print(f"学生{i+1}信息录入完成，信息为：学生姓名：{stu.name}年龄：{stu.age}，地址：{stu.add}")
print("所有学生信息录入完毕。")






















