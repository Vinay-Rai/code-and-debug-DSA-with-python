class Solution:
    def solve(self,index,total,subset,nums,target,result):
        if total == target:
            result.add(tuple(subset.copy()))
            return
        elif total>target:
            return
        
        if index>=len(nums):
            return
        sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index+1,sum,subset,nums,target,result)
        sum = total
        subset.pop()
        self.solve(index+1,sum,subset,nums,target,result)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        result = set()
        candidates.sort()
        self.solve(0,0,subset,candidates,target,result)
        newans = [list(x) for x in result]

        return newans




#OPTIMALL

class Solution:
    def solve(self,index,target,subset,candidates,result):
        if target == 0 :
            result.append(subset.copy())
            return
        if target <0:
            return
        if index>=len(candidates):
            return
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            subset.append(candidates[i])
            sum = target - candidates[i]
            self.solve(i+1,sum,subset,candidates,result)
            subset.pop()
        


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        result = []
        candidates.sort()
        self.solve(0,target,subset,candidates,result)
        
        return result