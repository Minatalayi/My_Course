
def rug (num):
   for i in range (num):
        for j in range (num):
            if (i %2 !=0 or j %2 !=0 ):
                print(" ☠️ ",end="")
            else:
                 print(" ☠️ ",end="")
        print()


num = int(input("please enter just a odd number: "))

rug(num)