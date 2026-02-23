#__str__字符串方法，可以通过它来将控制类转换为字符串
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #__str__魔术方法
    def __str__(self):
        return f"Student类对象,name={self.name},age={self.age}"
student=Student("胡家毅",18)
print(student)
print(str(student))

#__lt__小于符合比较方法，
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self, other):
        return self.age < other.age
stu1=Student("胡家毅",18)
stu2=Student("周逸",20)
print(stu1<stu2)
print(stu1>stu2)

#__le__小于等于比较符合方法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __le__(self, other):
        return self.age<=other.age
stu1=Student("胡家毅",18)
stu2=Student("周逸",20)
print(stu1<=stu2)
print(stu1>=stu2)

#__eq__比较运算符实现方法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __eq__(self, other):
        return self.age==other.age
stu1=Student("胡家毅",11)
stu2=Student("周逸",11)
print(stu1==stu2)











