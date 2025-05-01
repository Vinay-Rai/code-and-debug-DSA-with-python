nums = [30,3,5,6,8,9,10,20]

def is_sorted(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            return False
        
    return True

print(is_sorted(nums))


for i in range(len(nums)-1):
    nums.remove(nums[i+1])
print(nums)