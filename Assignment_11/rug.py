n=int(input("enter your number: "))

if n<=0:
    print("Invalid input")

elif n % 2 == 1:
      for i in range (n):
        for j in range (n):
            if (i %2 !=0 or j %2 !=0 ):
                print(" ☠️ ",end="")
            else:
                 print(" ☠️ ",end="")
        print()

                
elif n % 2 == 0:
    print("please enter a odd number")
