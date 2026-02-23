def test_retrun():
    return 1,2,3
x,y,z=test_retrun()
print(x)
print(y)
print(z)
def user_info(name,age,gender):
    print(f"您的名字是：{name},年龄是：{age},性别是：{gender}")
user_info(name="胡家毅",age="19",gender="男")

def user_info(*args):
    print(f"args的内容是{args}")
user_info("123","小美","女")

def user_info(**kwargs):
    print(kwargs)
user_info(name="胡家毅",age="19",gender="男")

def test_func(compute):
    result=compute(1,2)
    print(result)
def compute(x,y):
    return x+y


