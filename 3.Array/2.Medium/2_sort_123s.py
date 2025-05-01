#brute force

nums = [1,0,0,2,1,2,2,0,1,2]
# nums.sort()


# better
def sort_Colors(nums):
    zeros = 0
    ones = 0
    twos = 0
    for i in range(len(nums)):
        pass
        if nums[i]== 1:
            ones+=1
        elif nums[i]==2:
            twos+=1
        elif nums[i]==0:
            zeros+=1
    for i in range(len(nums)):
        if i<zeros:
            nums[i] = 0
        elif i < zeros + ones:
            nums[i] = 1
        else:
            nums[i] = 2
    
    return nums

print(sort_Colors(nums))


# optimal

