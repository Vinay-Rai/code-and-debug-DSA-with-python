#BRUTE FORCE

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        my_set = set()
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        total = nums[i] + nums[j] + nums[k] + nums[l]
                        if total == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            my_set.add(tuple(temp))
        result = []
        for ans in my_set:
            result.append(list(ans))
        return result
    

#BETTER

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        my_set = set()
        for i in range(0, n):
            for j in range(i + 1, n):
                hash_set = set()
                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hash_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        my_set.add(tuple(temp))
                    hash_set.add(nums[k])
        result = [list(ans) for ans in my_set]
        return result



#OPTIMAL

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        ans = []
        for i in range(ln):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,ln):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                right = ln-1
                left = j+1
                while left<right:
                    
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total>target:
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        ans.append(temp)
                        right-=1
                        left+=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1

                        while left<right and nums[right]==nums[right+1]:
                            right-=1


        return ans