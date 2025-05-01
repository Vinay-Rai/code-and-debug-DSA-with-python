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
    if target<nums[mid]:
        return mid
    elif target > nums[mid]:
        return mid + 1

print(binary_search([11,21,23,24,25,29],10))