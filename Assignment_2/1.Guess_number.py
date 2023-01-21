import random
computer_number=random.randint(1,99) 
guess_number=0
while True:
        guess_number=int(input("enter your guess: "))

        if guess_number==computer_number:
         print("you win")
         break
        elif guess_number>computer_number:
         print("go up")
        elif guess_number>computer_number:
         print("go down")
















