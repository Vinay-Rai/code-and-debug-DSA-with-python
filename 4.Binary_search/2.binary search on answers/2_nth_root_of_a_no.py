def nth_root(m,n):
    
    low = 1
    high = m
    while low<=high:
        mid = (high+low)//2
        
        if mid**n<= m:
            low = mid+1
        
        else:
            high = mid -1
    
    if high**n == m:

        return high
    else: 
        return -1


print(nth_root(1728,3))
