# brute force

def binarysubarray(nums,goal):
    n = len(nums)
    count = 0
    for i in range(0,n):
        total = 0
        for j in range(i,n):

            total +=nums[j]
            if total > goal:
                break
            if total == goal:
                count+=1
    return count


print(binarysubarray([1,0,1,0,1],2))