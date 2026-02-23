#基础数据类型注解
import random

var_1:int=10
var_2:str="胡家毅"
var_3:bool=True
#类对象类型注解
class Student:
    pass
stu:Student=Student()
#数据容器类型注解
my_list:list=[1,2,3]
my_dict:dict={"胡家毅":18}
my_set:set={1,2,3}
#容器类型详细注解
my_list1:list[int]=[1,2,3]
my_dict1:dict[str,int]={"胡家毅":18}
my_set1:set[int]={1,2,3}

random.randint(1,10)# type:int
dict={"周逸":20}#type:dict
#函数和方法的类型注解
































