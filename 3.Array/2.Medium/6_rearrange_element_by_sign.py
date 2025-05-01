def renumsange(nums):
    result = []
    n = len(nums)
    for i in nums:
        if i > 0:
            result.append(i)
    for i in nums:
        if i < 0:
            result.append(i)
    mid = n // 2
    i = 0
    j = mid
    count = 0
    while i < mid:
        nums[count] = result[i]
        count+=1
        nums[count]= result[j]
        count+=1
        i+=1
        j+=1
    print(nums)

print(renumsange([-1,1]))