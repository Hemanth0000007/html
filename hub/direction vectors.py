string = map(int,input().split())
mat = string.split('\n')
for i in range(1,7):
    for j in range(1,7):
        if mat[i][j] == '#':
            if mat[i-1][j-1] == '#' and  mat[i+1][j-1] == '#' and  mat[i+1][j+1] == '#':
             print(i+1,j+1)
            
