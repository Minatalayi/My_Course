
def lozi (n):
    for i in range(1, n+1):
        #print(n-i,'|', 2*i-1)
        print((n-i)*" "+(2*i-1)*"*")
    for i in range( 1, n+1):
        #print( i, '|',2*n-3 )
        print((i)*" "+(2*n-3)*"*")
        n-=1



row = int(input('enter row:'))
print()

lozi(row)