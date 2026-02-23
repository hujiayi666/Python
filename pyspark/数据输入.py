from  pyspark import SparkConf,SparkContext

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)
rdd1=sc.parallelize([1,2,3,4,5,6,7])
rdd2=sc.parallelize((1,2,3,4,5,6,7))
rdd3=sc.parallelize({"胡家毅":"18"})
rdd4=sc.parallelize({1,2,3,4,5,6,7})
rdd5=sc.parallelize("abcdefg")




print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())







sc.stop()












