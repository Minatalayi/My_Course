from Media_class import Media
from Film_class import Film
from Series_class import Series
from Clip_class import Clip
from Documantery_class import Documantary

OBJECTS=[]

def read_from_database():
    f=open("Assignment_12\database.txt.txt", "r")
    line = f.read().split("\n")
    for i in range (len(line)):
        result = line[i].split(",")
        if result[0]=="film":
            my_obj=Film(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        elif result[0]=="series":
            my_obj=Series(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        elif result=="clip":
            my_obj=Clip(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        elif result=="documentary":
            my_obj=Clip(result[0],result[1],result[2],result[3],result[4],result[5],result[6])

            OBJECTS.append(my_obj)

    f.close()
            
def write_to_database(OBJECTS):
    f = open("Assignment_12\database.txt.txt", "w")

    for x in OBJECTS:
        if x == "film":
            f.write(x.type + "," + x.name + "," + x.director + "," + x.imdb_score + "," + x.url + "," + x.duration + "," + x.casts + "\n")
        elif x.type == "series":
           f.write(x.type + "," + x.name + "," + x.director + "," + x.score + "," + x.url + "," + x.duration + "," + x.casts + "\n")
        elif x.type == "documentary":
            f.write(x.type + "," + x.name + "," + x.director + "," + x.score + "," + x.url + "," + x.duration + "," + x.casts + "\n")
        elif x.type == "clip":
            f.write(x.type + "," + x.name + "," + x.director + "," + x.score + "," + x.url + "," + x.duration + "," + x.casts + "\n")
    
    f.close() 

def show_menu():
    print("1: Add")
    print("2: Edit")
    print("3: Remove")
    print("4: Search")
    print("5: Show list")
    print("6: Show info")
    print("7: Download")
    print("8: Exit")
    print()
def add():
    x = input("Enter type: ")
    if x == "film":
        Film.add(OBJECTS)
    elif x == "series":
        Series.add(OBJECTS)
    elif x == "documentary":
        Documantary.add(OBJECTS)
    elif x == "clip":
        Clip.add(OBJECTS)

def edit():
        new_name = input("Enter name: ")
        for x in OBJECTS:
            if x.name == new_name:
                x.edit(OBJECTS, new_name)

def remove():
    new_name = input("Enter name: ")
    for x in OBJECTS:
        if x.name == new_name:
           x.remove(OBJECTS, new_name)

def search():
    x = input("Enter type: ")
    if x == "film":
        Film.search(OBJECTS)
    elif x == "series":
        Series.search(OBJECTS)
    elif x == "documentary":
            Documantary.search(OBJECTS)
    elif x == "clip":
            Clip.search(OBJECTS)

def show_list():
    for x in OBJECTS:
        if x.type == "film":
            Film.show_list(OBJECTS)
        elif x.type == "series":
            Series.show_list(OBJECTS)
        elif x.type == "documentary":
            Documantary.show_list(OBJECTS)
        elif x.type == "clip":
            Clip.show_list(OBJECTS)

def show_info():
    name1= input("Enter name: ")
    for x in OBJECTS:
        if x.name ==name1:
            x.show_info(OBJECTS,name1)

def download():
    name1 = input("Enter name: ")
    for x in OBJECTS:
        if x.name == name1:
            x.download(OBJECTS, name1)

def exit():
    write_to_database(OBJECTS)
    print("I hope see you soon")
    exit()

read_from_database()

while True:
    show_menu()
    choice=int(input("enter your choice: "))
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()    
    elif choice==6:
        show_info()
    elif choice==7:
        download()    
    elif choice==8:
        exit()
    else:
        print("TRY AGAIN...")







