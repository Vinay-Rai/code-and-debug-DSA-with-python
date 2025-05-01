def totalsum(nums,divisor):
    import math
    total  = 0
    for i in range(len(nums)):
        total = total + math.ceil(nums[i]/divisor)

    return total

def divisor(nums,threshold):
    low = 0
    high  = max(nums)
    ans = -1
    while low<=high:
        mid = (low+high)//2
        totalsums = totalsum(nums,mid)

        if totalsums <=threshold:
            ans = mid
            high = mid -1
            
        else:
            low = mid + 1
    
    return ans

print(divisor([44,22,33,11,1],5))



