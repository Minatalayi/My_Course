array=[]
len=int(input("enter the lenght of array: "))
for i in range(len):
    number=input("enter number: ")
    array.append(number)

copy_array=array
array.sort()

if copy_array==array:
 print("SORT")
else:
 print("NOT SORT")




