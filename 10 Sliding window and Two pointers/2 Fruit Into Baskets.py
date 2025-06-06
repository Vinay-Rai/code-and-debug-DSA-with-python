# brute force
def fruits_into_basket(arr):
    n = len(arr)
    max_length = 0
    for i in range(0,n):
        fruits = set()
        for j in range(i,n):
            fruits.add(arr[j])
            if len(fruits) > 2:
                break
            max_length = max(max_length,j-i+1)
    return max_length
    
print(fruits_into_basket([1,2,3,2,2]))


# better
def fruits(arr):
    left = 0
    right = 0
    max_length = 0
    fruits = {}
    n = len(arr)
    while right < n:
        fruits[arr[right]] = fruits.get(arr[right],0)+1
        while len(fruits)>2:
            fruits[arr[left]]-=1
            if fruits[arr[left]]==0:
                del fruits[arr[left]]
            left+=1
        if len(fruits)<=2:
            max_length = max(max_length,right-left+1)
        right+=1
    return max_length

print(fruits([3,3,3,1,2,1,1,3,3,4]))


# optimal

def fruits(arr):
    left = 0
    right = 0
    max_length = 0
    fruits = {}
    n = len(arr)
    while right < n:
        fruits[arr[right]] = fruits.get(arr[right],0)+1
        if len(fruits)>2:
            fruits[arr[left]]-=1
            if fruits[arr[left]]==0:
                del fruits[arr[left]]
            left+=1
        if len(fruits)<=2:
            max_length = max(max_length,right-left+1)
        right+=1 
    return max_length

print(fruits([3,3,3,1,2,1,1,3,3,4]))