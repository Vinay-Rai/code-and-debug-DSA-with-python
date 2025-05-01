def binary_search(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (high+low)//2
        
        if nums[mid]== target:
            return mid
        
        elif nums[mid]< target:
            low = mid+1
        
        else:
            high = mid -1
    
    return -1

print(binary_search([1,2,3,4,5],5))


# RECURSIVE SOLUTION
def binary_search_recursive(nums,low,high,target):
    if low > high:
        return -1
    mid = (low+high)//2

    if nums[mid]==target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums,mid+1,high,target)
    
    else:
        return binary_search_recursive(nums,low,mid-1,target)
    

nums = [1,2,3,4,5]
print(binary_search_recursive(nums,0,len(nums)-1,6))