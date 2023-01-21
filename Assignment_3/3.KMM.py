num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
a = num1
b = num2
while(num2 != 0):  
    temp = num2
    num2 = num1 % num2  
    num1 = temp
gcd = num1  
lcm = (a * b) // gcd  
print(lcm)