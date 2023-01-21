def fibonachi(n):
  n=int(input("enter your number"))
  

  if n<=0:
   print(" incorrect input") 
  elif  n==0:
    return 0
  elif n==1:
     return 1
  else:
   return fibonachi(n-1)+fibonachi(n-2)
print(fibonachi())
