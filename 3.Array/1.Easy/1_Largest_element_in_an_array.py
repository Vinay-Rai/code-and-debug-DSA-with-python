
nums = [55,32,-97,99,3,67]

#lg_elem = nums[0]
# lg_elem = float("inf")

lg_elem = float("-inf")
for i in range(1,len(nums)):
    if nums[i] > lg_elem:
        lg_elem = nums[i]
print(lg_elem)



#This is efficient compare to above code
def getLargestNum(nums):
    print(max(nums))
    return max(nums)

getLargestNum([34,18,21])



def largest(arr):
    lg = arr[0]
    for i in range(1,len(nums)):
        lg = max(lg , arr[i])
    return lg

print(largest(nums))