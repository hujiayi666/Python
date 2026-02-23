class student:
    name=None
    def say_hi(self):
        print(f"大家好，我是{self.name}")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")

stu=student()
stu.name="胡家毅"
stu.say_hi2("不错哦")
stu1=student()
stu1.name="周逸"
stu1.say_hi2("包的啊")
















































