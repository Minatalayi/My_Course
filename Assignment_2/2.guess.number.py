import random
result=random.randint(1,99)
guess=input("what is your guess? ")
guess=int(guess)
while guess!=result:
    if guess>result:
        print("go down")
    else:
     print("go up")
    guess=input("what is your guess? ")
    guess=int(guess)


print("you win") 
