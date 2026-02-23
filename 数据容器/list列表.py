mylist=[1,2,3,4,5,6,7,8,9,10]
i=0
list1=[]
while i<len(mylist):
    x=mylist[i]
    if x%2==0:
      list1.append(x)
    i+=1
print(list1)

mylist=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for x in mylist:
    if x%2==0:
       list2.append(x)
print(list2)




