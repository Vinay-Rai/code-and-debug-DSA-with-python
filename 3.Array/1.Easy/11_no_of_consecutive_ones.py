def conse(nums):

    n = len(nums)
    ones = 0
    count = 0
    for i in range(n):
        if nums[i] == 0:
            ones = max(ones,count)
            count = 0
        else:
            count+=1
    return max(ones,count)

print(conse([1,1,0,1,1,1,1,1,0,0,0,1]))