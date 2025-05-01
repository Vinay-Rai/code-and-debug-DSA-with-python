def search( nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2  
        
        if nums[mid] == target:  
            return mid
        
       
        if nums[low] <= nums[mid]:
            
            if nums[low] <= target <= nums[mid]:
                high = mid - 1  
            else:
                low = mid + 1  
        
        else:
            
            if nums[mid] <= target <= nums[high]:
                low = mid + 1  
            else:
                high = mid - 1 
    
    return -1 

print(search([7,7,7,7,7,7,7,1,2,3,4,5,7,7],7))