nums = [1,0,2,4,3,0,0,3,5,1]

for i in range(len(nums)):
    if nums[i] == 0:
        nums.remove(nums[i])
        nums.append(0)

print(nums)