
def mul(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end=" ")
        print()
row=int(input("please enter row: ")) 
col=int(input("please enter col: "))
mul(row,col)   