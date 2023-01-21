from termcolor import colored
import random
import time


O=colored("O","blue")
X=colored("X","red")


def show_game_board():

 for i in range(3):
   for j in range(3):
     print(game[i][j], end=" ")
   print()

def check():
      if game[0][0]==game[0][1]==game[0][2]=="X":
         print("player 1 win")
         exit
      elif game[0][0]==game[0][1]==game[0][2]=="O":
           print("player 2 win")
           exit
      elif game[1][0]==game[1][1]==game[1][2]=="X":
           print("player 1 win")
           exit
      elif game[1][0]==game[1][1]==game[1][2]=="O":
           print("player 2 win")
           exit
      elif game[2][0]==game[2][1]==game[2][2]=="X":
         print("player 1 win")
         exit
      elif game[2][0]==game[2][1]==game[2][2]=="O":
         print("player 2 win")
         exit
      elif game[0][0]==game[1][0]==game[2][0]=="X":
         print("player 1 win")
         exit
      elif game[0][0]==game[1][0]==game[2][0]=="O":
         print("player 2 win")
         exit
      elif game[0][1]==game[1][1]==game[2][1]=="X":
         print("player 1 win")
         exit
      elif game[0][1]==game[1][1]==game[2][1]=="O":
         print("player 2 win")
         exit     
      elif game[0][2]==game[1][2]==game[2][2]=="X":
         print("player 1 win")
         exit
      elif game[0][2]==game[1][2]==game[2][2]=="O":
         print("player 2 win")
         exit
      elif game[0][0]==game[1][1]==game[2][2]=="X":
         print("player 1 win")
         exit
      elif game[0][0]==game[1][1]==game[2][2]=="O":
         print("player 2 win")
         exit
      elif game[0][2]==game[1][1]==game[2][0]=="X":
          print("player 1 win")
          exit  
      elif game[0][2]==game[1][1]==game[2][0]=="O":
         print("player 2 win")
         exit

game=[["-","-","-"],
      ["-","-","-"],
      ["-","-","-"]]

show_game_board()

while True:

   print("player 1")
   while True:
      row=int(input("satre morede nazareto begoo:  "))
      col=int(input("sotoone morede nazareto benevis:  ")) 
      if 0<=row<=2 and 0<=col<=2:
         if game[row][col]=="-":
            game[row][col]="X"
            break
         else:
            print("khali nist")
      else:
         print("try again")

   show_game_board()
   check()
   print("player2")
   while True:
      row=int(input("satre morede nazareto begoo:  "))
      col=int(input("sotoone morede nazareto benevis:  "))
      if 0<=row<=2 and 0<=col<=2:
         if game[row][col]=="-":
            game[row][col]="O"
            break
         else:
            print("khali nist")
      else:
         print("try again")
   show_game_board()
   check()



