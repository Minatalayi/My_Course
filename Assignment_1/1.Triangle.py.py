print("a,b,c are three sides of a triangle")

    
a=float(input("please enter 1st side: "))
b=float(input("please enter 2st side: "))
c=float(input("please enter 3st side: "))


if a+b>c and a+c>b and b+c>a:
    print("it can be a triangle")
else:
    print("it CANT be a triangle")

