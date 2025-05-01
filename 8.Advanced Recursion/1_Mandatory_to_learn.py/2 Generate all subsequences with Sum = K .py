def solve( index, subset, nums, result,target):
        # Base case: if we've considered all elements, store the current subset
        if index >= len(nums):
            if sum(subset) == target:
                result.append(subset.copy())
            return
        
        # Choice 1: Include the current element
        subset.append(nums[index])
        solve(index + 1, subset, nums, result,target)
        
        # Backtrack: remove the last element before exploring the next choice
        subset.pop()
        
        # Choice 2: Exclude the current element and move forward
        solve(index + 1, subset, nums, result,target)

def subsets( nums,target):
    result = []
    solve(0, [], nums, result,target)
    return result

print(subsets([1,2,3,4],5))



# sir wala



def backtrack(subset, index, total):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    Sum = total + nums[index]
    backtrack(subset, index + 1, Sum)
    e = subset.pop()
    Sum -= e
    backtrack(subset, index + 1, Sum)




result = []
nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]
k = 3
backtrack([], 0, 0)
print(result)