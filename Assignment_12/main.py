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

















