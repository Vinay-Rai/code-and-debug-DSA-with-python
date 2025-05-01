matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rows = len(matrix)
cols = len(matrix[0])
result = [[0]*rows for _ in range(cols)]
k = 0
for i in range(rows-1,-1,-1):
    for j in range(cols-1,-1,-1):
        result[j][k]=matrix[i][j]
    k+=1

for i in range(rows):
    for j in range(cols):
        print(result[i][j],end=" ")
    print()
        