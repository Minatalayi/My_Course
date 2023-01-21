list=[]
list_inverse=[]

len_list=int(input("please enter lenght of the list: "))

for i in range(len_list):
    number=int(input("please enter the number: "))
    list.append(number)

x=len_list-1 
while x>=0:
  list_inverse.append(list[x])
  x-=1

print(list)
print(list_inverse)  