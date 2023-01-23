import os.path
from os import path
import gtts
from playsound import playsound



def read_from_file():
    global words_bank
    f=open("translate.txt","r")
    words_bank=[]
    temp=f.read().split("\n")
    for i in range(0,len(temp),2):
        my_dict={"en":temp[i],"fa":temp[i+1]}
        words_bank.append(my_dict)

    f.close()

def english_to_persian():
    user_text=input("enter your english text: ")
    user_words=user_text.split(" ")

    for user_word in user_words:
        for word in words_bank:
            if user_word==word["en"]:
               output=output+word["fa"]+" "
            break
        else:
             output=output+user_word+" "
    print(output)

def persian_to_english():
    user_text = input("Enter your persian text:")
    user_words=user_text.split(" ")
    for user_word in user_words:
        for word in words_bank:
            if user_word==word["fa"]:
                output=output+word["en"]+" "
            break
        else:
             output=output+user_word+" "
    print(output)

    s=gtts.gTTS(output,lang="en",slow=False)
    s.save("voice.mp3")
    
    playsound("voice.mp3")

def add_database():
    file_name=input("Please enter new word: ")
    if path.exists(file_name):
        x= open("translate.txt", "a")
        new_word_en=input("Please enter your english word:")
        for word in words_bank:
            if new_word_en==word["en"]:
                print("Try again \n")
                break
        else:
            new_word_fa=input("Please enter pesian word: ")
            x.write("\n"+new_word_en+"\n"+new_word_fa)
            print("Well done \n")
        x.close()



def show_menu():
    print("welcome")
    print("1-en to fa")
    print("2_fa to en")
    print("3_add new word")
    print("exit")

read_from_file()

while True:
    show_menu()
    choice=int(input("enter your choice: "))

    if choice==1:
        english_to_persian()
    elif choice==2:
        persian_to_english()    
    elif choice==3:
        add_database()
    elif choice==4:
        exit(0)
