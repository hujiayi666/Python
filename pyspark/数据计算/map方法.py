from pyspark import SparkConf,SparkContext
import os
#os.environ['PYSPARK_PYTHON']="C:\Users\Public\Desktop\PyCharm 2023.2.1.lnk"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)
#准备一个rdd
rdd=sc.parallelize([1,2,3,4,5])
#通过map方法将全部数据都乘以10
def func(data):
    return data*10

rdd1=rdd.map(func)
#(T)->U
#(T)->T
print(rdd1)












