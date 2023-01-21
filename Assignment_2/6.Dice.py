import random
while True:
    b=input("enter a for start: ")
    if b=="a":
        a=random.randint(1,6)
        print(a)
        if a<6:
            break