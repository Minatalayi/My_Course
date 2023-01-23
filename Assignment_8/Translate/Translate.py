def read_from_file():
    f=open("Assignment_8/translate.txt", "r")
    print(f)
    words=[]
    for line in f:
        words.append(line)
    print(words)    