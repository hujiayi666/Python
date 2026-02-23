"""编程输出1000以内所有能同时被3和4整除的数，以及这些数的个数、这些数的和"""
list=[]
count=0
s=0
for i in range(1,1001):
    if i%3==0 and i%4==0:
        list.append(i)
        count=count+1
        s=s+i
print(f"1000以内所有能同时被3和4整除的数如下{list}")
print(f"这些数的个数为:{count},和为:{s}")