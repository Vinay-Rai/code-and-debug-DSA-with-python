def solve(arr,k):
    import copy
    for i in range(len(arr)-k-1):
        j=i
        m=0
        new_arr = copy.deepcopy(arr)
        while m < k:
            new_arr[j]=new_arr[j]*-1
            new_ser = set(new_arr)
            if len(new_ser)==1:
                return True
            m+=1
            j+=1
    return False
    
print(solve([1,-1,1,-1,1],3))