import time
import datetime
print('send the time in order')
H=int(input("enter Hour: "))
M=int(input("enter Minute: "))
S=int(input("enter Second: "))

x=H*60
y=x+M
T=y*60+S
print("Second=  ",T)
