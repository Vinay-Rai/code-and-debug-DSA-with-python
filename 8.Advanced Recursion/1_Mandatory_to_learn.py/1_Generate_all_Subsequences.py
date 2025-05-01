def solve( index, subset, nums, result):
        # Base case: if we've considered all elements, store the current subset
        if index >= len(nums):
            result.append(subset.copy())
            return
        
        # Choice 1: Include the current element
        subset.append(nums[index])
        solve(index + 1, subset, nums, result)
        
        # Backtrack: remove the last element before exploring the next choice
        subset.pop()
        
        # Choice 2: Exclude the current element and move forward
        solve(index + 1, subset, nums, result)

def subsets( nums):
    result = []
    solve(0, [], nums, result)
    return result

print(subsets([1,2,3]))




