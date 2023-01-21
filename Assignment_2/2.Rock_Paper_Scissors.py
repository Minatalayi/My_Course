import random
print("welcome to the GAME")
print("your choices can be: ")
print("1=rock")
print("2=paper")
print("3=scissors")
for i in range(5):

    computr_score=0
    user_score=0

    while computr_score<5 and user_score<5:
        x=random.randint(1,3)

    if x==1:
        computer="rock"
    elif x==2:
        computer="paper"
    elif x==3:
        computer="scissors"

    user=input(("enter your choice"))
            

    if computer=="rock" and user=="paper":
        print("user win")
        user_score=user_score+1

    elif computer=="rock" and user=="scissors":
        print("computer win")
        computr_score=computr_score+1

    elif computer=="rock" and user=="rock":
        print("you tied")

    elif  computer=="paper" and user=="rock":
        print("computer win")
        computr_score=computr_score+1

    elif computer=="paper" and user=="scissors":
        print("user win")
        user_score=user_score+1

    elif computer=="paper" and user=="paper":
        print("you tied")

elif computer=="scissors" and user=="paper":
    print("computer win")
    computr_score=computr_score+1

elif computer=="scissors" and user=="rock":
    print("user win")
    user_score=user_score+1

elif computer=="scissors" and user=="scissors":
    print("you tied")

print("computer_score",computr_score)    
print("user_score",user_score)
