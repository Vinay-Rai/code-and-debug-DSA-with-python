def search( nums):
    n = len(nums)
    low = 0
    high = n - 1
    mins = float("inf")
    
    while low <= high:
        mid = (low + high) // 2  
        
       
        if nums[low] <= nums[mid]:
            mins = min(mins,nums[low])
            low = mid + 1 
        
            
        elif nums[mid] <=  nums[high]:
            mins = min(mins,nums[mid])
            high = mid - 1
                
    
    return mins

print(search([3,4,5,6,7,8]))