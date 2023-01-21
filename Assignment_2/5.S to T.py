import time
S=int(input("enter your time in seconds: "))
H=S//3600
print('Hour: ',H)
x=S%3600
M=x//60
print("Minute: ",M)
S=x%60
print("Second: ",S)
