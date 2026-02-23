#导包
from pyspark import SparkConf,SparkContext
#创建Sparkconf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于Sparkconf类对象创建Sparkcontext对象
sc=SparkContext(conf=conf)
#打印pyspark的运行版本
print(sc.version)
#停止Sparkcontext对象的运行
sc.stop()










































