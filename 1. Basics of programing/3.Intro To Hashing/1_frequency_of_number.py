def frequency(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

arr = [1,1,1,2,5,6,7,4,2,4,5]
print(frequency(arr))


hash_map = {}
n = len(arr)
for i in range(0,n):
    hash_map[arr[i]]=hash_map.get(arr[i],0)+1

print(hash_map)


