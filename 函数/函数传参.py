#乘法运算
def test_func1(cheng):
    reslut=cheng(2,3)
    print(reslut)
def cheng(x,y):
    return x*y
test_func1(cheng)
#加法运算
def test_func2(jia):
    result=jia(1,2)
    print(result)
def jia(x,y):
    return x+y
test_func2(jia)
#减法运算
def test_func3(jian):
    result=jian(2,1)
    print(result)
def jian(x,y):
    return x-y
test_func3(jian)
#除法运算
def test_func4(chu):
    result=chu(2,1)
    print(result)
def chu(x,y):
    return x/y
test_func4(chu)


while True:
      x=int(input("输入自变量："))
      y=int(input("输入应变量："))
      result=x+y
      print(result)



