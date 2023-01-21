def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = int(input("enter firs number:  "))
b = int(input("enter second number:  "))
 

print ("The gcd of a and b is : ",end="")
print (computeGCD(a, b))