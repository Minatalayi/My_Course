n=int(input("enter row: "))
matrix=[[1 for i in range(n)] for ij in range(n)] 

for i in range(n):
    for j in range(1,i):

        matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-1]

for i in range(n):
    for j in range( i+1 ):
        print(matrix[i][j], end=' ')
    print()
  
