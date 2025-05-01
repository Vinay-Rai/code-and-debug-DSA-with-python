def sell(nums):
    n = len(nums)
    profit = float("-inf")
    for i in range(n-1):
      for j in range(i+1,n):
         profit = max(nums[j]-nums[i],profit)
    if profit < 0:
       return 0 
    return profit 


print(sell([7,6,4,3,1]))
      