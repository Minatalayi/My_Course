list=[]
list_cut=[]

len_list=int(input("please enter lenght of the list: "))

for i in range(len_list):
    number=int(input("please enter the number: "))
    list.append(number)

for part in list:
    if part not in list_cut:
        list_cut.append(part)

print(list)
print(list_cut)        