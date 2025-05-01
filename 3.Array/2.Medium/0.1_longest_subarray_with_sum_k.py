
def longest_sub_aray(arr,k):
    length = 0
    for i in range(len(arr)):
        sum = 0
        count = 0
        for j in range(i,len(arr)):
            sum+=arr[j]
            count+=1
            if sum == k:
                length  = max(length,count)
    return length


arr = [10, -10, 20, 30]
k = 5
print(longest_sub_aray(arr,k))