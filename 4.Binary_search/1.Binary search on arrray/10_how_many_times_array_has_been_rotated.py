def search( arr):
    n = len(arr)
    low = 0
    high = n - 1
    mins = float("inf")
    prevmin = float("inf")
    index = 0
    
    while low <= high:
        mid = (low + high) // 2  
        
       
        if arr[low] <= arr[mid]:
            prevmin = mins
            mins = min(mins,arr[low])
            if prevmin != mins:
                index = low
            low = mid + 1 
        
            
        elif arr[mid] <=  arr[high]:
            prevmin = mins
            mins = min(mins,arr[mid])
            if prevmin != mins:
                index = mid

            high = mid - 1
                
    
    return index

print(search([9,10,11,3,4,5,6,7,8]))