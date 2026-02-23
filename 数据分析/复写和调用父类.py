class Phone:
    ID=None
    producer="周逸"

    def call_by_5g(self):
        print("使用5g通话")
#定义子类，复写父类成员
class Phone2022(Phone):
    producer = "胡家毅"    #复写父类成员属性

    def call_by_5g(self):  #复写父类成员功能
        print("开启CPU单核模式，确保通话是省电")
        print("使用5g网络通话")
myphone=Phone2022()
print(myphone.producer)
myphone.call_by_5g()




class Phone:
    ID=None
    producer="周逸"

    def call_by_5g(self):
        print("使用5g通话")
#定义子类，复写父类成员
class Phone2022(Phone):
    producer = "胡家毅"    #复写父类成员属性

    def call_by_5g(self):  #复写父类成员功能
        print("开启CPU单核模式，确保通话是省电")
        #方法1
        Phone.call_by_5g(self)
        print(f"生成商是{Phone.producer}")
        #方法2
        print(f"生产商是{super().producer}")
        super().call_by_5g()
myphone=Phone2022()
print(myphone.producer)
myphone.call_by_5g()


















