def getFloorAndCeil(a,x):
    floor = -1
    ceil = -1
    n = len(a)
    low, high = 0, n - 1  

    while low <= high:
        mid = (low + high) // 2  # Find mid index

        if a[mid] == x:
            return [x, x]  # If exact match, floor and ceil are the same
        
        elif a[mid] > x:
            ceil = a[mid]  # Update ceil (smallest number ≥ x)
            high = mid - 1  # Move left to find a smaller valid ceil
        
        else:
            floor = a[mid]  # Update floor (largest number ≤ x)
            low = mid + 1  # Move right to find a larger valid floor

    return [floor, ceil]

print(getFloorAndCeil([11,21,23,24,25,29],12))