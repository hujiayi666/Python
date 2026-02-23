def twoSum(self, nums, target):
    resault=[]
    map1={}
    for i in range(0,len(nums)):
        map1.pop(nums[i],i)
    for j in range(0,len(nums)):
        diffrence=target-nums[j]
        if map1.keys(diffrence) and map1.values(diffrence)!=j:
            resault[0]=j
            resault[1]=map1.values(diffrence)
            return resault

