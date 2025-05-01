def majority(nums):
    import math
    n= len(nums)
    d={}
    n = math.ceil(len(nums)/2)
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if d[i]>=n:
            # print(n)
            return i
    print(d)

print(majority([1,1,2,2,1,1,2]))
