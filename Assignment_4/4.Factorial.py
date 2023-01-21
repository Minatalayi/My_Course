number=int(input("please enter your number: "))
n=number

while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n/=i
    else:      
        break

if n==1:
        print("yes")
else:
        print("no")
            
