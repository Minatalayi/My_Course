name=input("please enter your name: ")
family=input("please enter yor family: ")
grade1=float(input("please enter yor 1st grade: "))
grade2=float(input("please enter your 2st grade: "))
grade3=float(input("please enter your 3st grade: "))

average=(grade1+grade2+grade3)/3
if average>=17:
    print("GREAT")
elif average>=12 and average<17:
    print("NORMAL")
elif average<12:
    print("FAIL")
    