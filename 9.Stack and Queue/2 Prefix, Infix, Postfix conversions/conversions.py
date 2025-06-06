# brute force by me
def greater_element(nums1, nums2):
    result = []
    for num in nums1:
        ind = nums2.index(num)
        found = False
        for i in range(ind + 1, len(nums2)):
            if nums2[i] > num:
                result.append(nums2[i])
                found = True
                break
        if not found:
            result.append(-1)
    return result

nums1 = [2,4]
nums2 = [1,2,3,4]
print(greater_element(nums1,nums2))



# by sir
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n:
                if stack:
                    result[i] = stack[-1]
            stack.append(nums[i % n])
        return result
    

# chat gpt jo leetcode ka question hai uska answer


def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}

    # Process nums2 to find the next greater element for each number
    for num in nums2:
        # Pop smaller elements from stack and map them to the current num
        while stack and num > stack[-1]:
            smaller = stack.pop()
            next_greater[smaller] = num
        stack.append(num)

    # For remaining elements in the stack, no greater element exists
    for num in stack:
        next_greater[num] = -1

    # Build result for nums1 using the dictionary
    result = []
    for num in nums1:
        result.append(next_greater[num])

    return result
