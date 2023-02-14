import random
num=int(input("choice a number between 1 & 50: "))
ch_system=random.randint(1,50)
while ch_system!=num:
    if ch_system>num:
        you=print("boro bala")
        ch_system=random.randint(0,ch_system-1)
        print(ch_system)
        
    else:
        you=print("boro payeen")
        ch_system=random.randint(ch_system+1,50)
        print(ch_system)     

    print("horaaaa bordi")
