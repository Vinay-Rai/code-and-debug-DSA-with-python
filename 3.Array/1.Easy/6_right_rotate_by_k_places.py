nums = [1,2,3,4,5]
n = len(nums)
k = int(input("enter no. "))
k = k % n
num1 = nums[:n-k]
num2 = nums[n-k:]
# nums = num2 + num1

nums[:] = num2 + num1  #inplace usi array me change


# nums = num2
# nums.extend(num1)
# nums = num2.extend(num1)
print(nums)
# print(num2,num1)


nums = [1,2,3,4,5]
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0] = temp
print(nums)