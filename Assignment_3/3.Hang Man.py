import random

user_mistakes=0

words_bank=["tree","book","orange","fish","dog","cat","apple","pilow","pink","sky","people","accounting"]
true_chars=[]
false_chars=[]

x=random.randint(0,len(words_bank)-1)
word=words_bank[x]
word=word.lower()
while True:
    for i in range(len(word)):
        if word[i] in true_chars:
            print(word[i], end="")
        else:
            print("-",end="")

    user_char=input("please write your guess: ")   
    user_char=user_char.lower()  

    if user_char in word:
        true_chars.append(user_char)
    else:
        false_chars.append(user_char)
        user_mistakes+=1
        print('number of mistakes: ',user_mistakes)
    if len(true_chars)==len(word):
        print("YOU WIN")
        break
    elif user_mistakes==6:
        print("GAME OVER")
        break
