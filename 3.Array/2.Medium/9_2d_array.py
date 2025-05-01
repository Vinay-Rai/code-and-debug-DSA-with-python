nums = [[5,20,3],[7,-10,9],[1,-52,6]]

rows = len(nums)
cols = len(nums[0])
for i in range(rows):
    for j in range(cols):
        print(nums[i][j],end=" ")
    print()



# upper triangle
for i in range(rows):
    for j in range(cols):
        if j>=i:
            print(nums[i][j],end="   ")
        else:
            print("*",end="   ")
    print()



# lower triangle
for i in range(rows):
    for j in range(cols):
        if i>=j:
            print(nums[i][j],end="   ")
        else:
            print("*",end="   ")
    print()



# diagonal
for i in range(rows):
    for j in range(cols):
        if i+j== rows-1:
            print(nums[i][j],end="   ")
        else:
            print("*",end="   ")
    print()


# transpose of matrix
result = [[0]*rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        result[j][i]=nums[i][j]
        
print(result)