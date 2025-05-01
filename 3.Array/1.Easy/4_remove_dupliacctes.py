
# working hai but set(nums) extra space leta hai
nums = [1,1,2]
n = len(nums)
nums = list (set(nums))
nums.sort()
new_l = len(nums)
for i in range(n-new_l):
    nums.append(-1)
print(nums)
print(new_l)

