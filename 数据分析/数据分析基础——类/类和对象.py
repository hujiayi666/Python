#设计一个闹钟类
class clock:
    id=None     #序列号
    price=None  #价格
#调用winsound来模拟声音
    def ring(self):
        import winsound    #导包
        winsound.Beep(2000,3000)
#创建对象
clo1=clock()
#传参
clo1.id=1001
clo1.price=19.9
clo1.ring()
print(f"闹钟的序列号为{clo1.id}，价格为{clo1.price}")
#创建对象
clo2=clock()
#传参
clo2.id=1002
clo2.price=21
clo2.ring()
print(f"闹钟的序列号为{clo2.id}，价格为{clo2.price}")


























