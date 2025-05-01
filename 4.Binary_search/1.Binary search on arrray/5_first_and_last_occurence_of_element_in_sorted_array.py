# brute force linear search
def searchRange(nums, target) :
    first = -1
    last = -1
    
    for i in range(len(nums)):  # Iterate through the entire array
        if nums[i] == target:
            if first == -1:  # First occurrence is found
                first = i
            last = i  # Update last occurrence
    
    return [first, last]  # Return final result





# Optimal


def lowerBound(arr, k):
    n = len(arr)
    lb = -1  # Initialize floor index as -1
    low, high = 0, n - 1  

    while low <= high:
        mid = (low + high) // 2  # Find mid index

        if arr[mid] >= k:
            lb = mid  # Update floor index
            high = mid - 1  # Move left to find a smaller element
        else:
            low = mid + 1  # Move right to find a larger floor

    return lb
    

def upperBound(arr, x):
    n = len(arr)
    ub = n  # Default upper bound if no element is greater than x
    low, high = 0, n - 1  

    while low <= high:
        mid = (low + high) // 2  # Find mid index

        if arr[mid] > x:
            ub = mid  # Update upper bound
            high = mid - 1  # Move left to find a smaller valid index
        else:
            low = mid + 1  # Move right to search for a larger element

    return ub-1

