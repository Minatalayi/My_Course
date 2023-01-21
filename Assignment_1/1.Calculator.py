import math
print("welcome to my calculator")

while True:
        print("+ : sum")
        print("_ : min")
        print("* : mul")
        print("/ : div")
        print("sin")
        print("cos")
        print("tan")
        print("cot")
        print("sqrt")
        print("factorial")
        print=("exit")
        print("**************")
        op=input("please enter your choose: ")

        if op=="exit":
         print("the end")
         break


        elif op=="+" or op=="_" or op=="*" or op=="/":
         a=float(input("enter first number: "))
         b=float(input("enter second number: "))

        elif op=="sin" or op=="cos" or op=="tan" or op=="cot":
         a=float(input("enter your number: "))
        degree=a*180/math.pi

        elif op=="sqrt" or op=="factorial":
        a=int(input("enter your number: "))
        else:
        result="operator not found"

        if op=="+":
         result=a+b
         print(result)   
        elif op=="_":
         result=a-b
         print(result)
        elif op=="*":
         result=a*b
         print(result)
        elif op=="/":
         if b==0:
          result="cannot divide by zero"
          print(result)
        else:
          result=a/b
          print(result)

        elif op=="sin":
        result=math.sin(degree)
        elif op=="cos":
        result=math.cos(degree)
        elif op=="tan":
        result=math.tan(degree)
        elif op=="cot":
        result=math.cot(degree)
        elif op=="sqrt":
        result=math.sqrt(a)
        elif op=="factorial":
        result=math(a)

print("result= ",result)
