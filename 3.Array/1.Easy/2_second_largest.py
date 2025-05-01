nums = [55,67,32,-97,99,3]

lg_elem = float("-inf")
lg_i = 0
for i in range(1,len(nums)):
    if nums[i] > lg_elem:
        lg_elem = nums[i]
        lg_i = i
print(lg_elem)
nums[lg_i] = nums[0]

lg_sec_elem = float("-inf")
for i in range(1,len(nums)):
    if nums[i] > lg_sec_elem:
        lg_sec_elem = nums[i]
        lg_i = i
print(lg_sec_elem)



#optimal this is think by me
nums = [55,67,32,-97,99,3]
first = float("-inf")
second = float("-inf")
for i in range(len(nums)):
    if nums[i] > first:
        second = first
        first = nums[i]
    elif nums[i] > second and nums[i]<first:
        second = nums[i]
print(first,second)





# brute force
# using sort

nums = [55,67,32,-97,99,3]
nums.sort()
print(nums[-2])



#better
nums = [55,32,-97,99,3,67]
lg_elem = float("-inf")
second_largest = float("-inf")
for i in range(1,len(nums)):
    lg_elem = max(lg_elem , nums[i])

for i in range(len(nums)):
    if nums[i] > second and nums[i] != lg_elem:
        second = nums[i]
