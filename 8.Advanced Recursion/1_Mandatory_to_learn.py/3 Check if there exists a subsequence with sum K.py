# subset wala code hata sakte ho

def backtrack(subset, index, total):
    if total == k: 
        result.append(subset.copy())  
        return True  

    if index >= len(nums): 
        return False

    subset.append(nums[index])  
    Sum = total + nums[index]  

    pick = backtrack(subset, index + 1, Sum)  

    if pick:  
        return True
    
    e = subset.pop()
    Sum = total

    return backtrack(subset, index + 1, Sum) 

result = []
nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]
k = 3

backtrack([], 0, 0)
print(result)