nums = [1,2,3,4,5]
# pop = nums.pop()
# nums.insert(0,pop)
# print(nums)


#using loops
n = len(nums)
elem = nums[n-1]
for i in range(n-1,0,-1):
    nums[i] = nums[i-1]
nums[0] = elem
# print(nums)


# using python power

nums = [1,2,3,4,5]
n = len(nums)
# nums = nums[-1] + nums[0:n-1]
 

#iski wajah se nums ka address change nahi hoga ye inlce slicing ho gayi
# nums[:] = nums[-1:] + nums[0:n-1] 
nums[:] = nums[n-1:] + nums[0:n-1] 


print(nums)

