def solve(binary, index,subset,result,n):
    if index >= n:
        result.append(subset.copy())
        return
    subset.append(binary)
    solve(binary,index+1,subset,result,n)
    subset.pop()
    solve(binary^1,index+1,subset,result,n)





def binaries(result):
    result=[]
    solve(0,0,[],result,3)
    return result
print(binaries([]))

        
        