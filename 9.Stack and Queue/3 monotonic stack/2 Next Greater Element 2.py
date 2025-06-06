def nextGreaterElements( nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range( n - 1, -1, -1):
        while len(stack) != 0 and stack[-1] <= nums[i]:
            stack.pop()

        if len(stack)!=0:
                result[i] = stack[-1]
        if len(stack)==0:
             for j in range(0,i):
                if nums[j]>nums[i]:
                     result[i] = nums[j]
                     break
        stack.append(nums[i])
    return result


print(nextGreaterElements([1,2,1]))