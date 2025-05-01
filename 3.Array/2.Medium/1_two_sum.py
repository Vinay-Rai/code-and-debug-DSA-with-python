# brute force solution

def two_sum(nums,target):

    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]

print(two_sum(nums = [2,7,11,15], target = 9))



# optimal
def twosum_optimal(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i


print(twosum_optimal(nums = [2,7,11,15], target = 9))
    