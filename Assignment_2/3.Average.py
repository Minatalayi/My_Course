sum=0
score_counter=0
while True:
    score=input("enter your score or type EXIT:   ")
    if score=="EXIT":
        break
    else:
        sum+=float(score)
    score_counter+=1
print("your average= ",sum/score_counter)
