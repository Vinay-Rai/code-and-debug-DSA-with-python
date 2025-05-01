#brutefprce

def leaders(arr):
    result = []
    n = len(arr)
    
    for i in range(n):
      
        # Check elements to the right
        for j in range(i + 1, n):
          
            # If a larger element is found
            if arr[i] < arr[j]:
                break
        else:
            # If no larger element was found
            result.append(arr[i])
    
    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))




# optimal
def leaders_in_array(nums):
    result = []
    maxi = float("-inf")
    n = len(nums)
    for i in range(n-1,-1,-1):
        # e = max(nums[i],maxi)
        # if e > maxi:
        if nums[i]>= maxi:
            result.append(nums[i])
            # maxi = e
            maxi = nums[i]
    result.reverse()
    return result

print(leaders_in_array([5,4,3,2,1]))

