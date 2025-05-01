def missing_no(nums):

    n = len(nums)
    total_sum = int(n*((n+1)/2))
    sum = 0
    for i in range(n):
        sum+=nums[i]
    return total_sum - sum

print(missing_no([0,1])) 