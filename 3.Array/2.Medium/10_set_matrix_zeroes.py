matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
r = {}
c = {}
rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if matrix[i][j]==0:
            r[i] = 0
            c[j] = 0


rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if i in r:
            matrix[i][j]=0
        elif j in c:
            matrix[i][j]=0



rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()

