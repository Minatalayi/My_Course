import random
random_array=[]
len=int(input("enter the lenght of array: "))
for i in range(len):
    x=random.randint(0,100)
    if x not in random_array:
        random_array.append(x)
print(random_array)        