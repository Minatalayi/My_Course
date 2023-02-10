import pytube

class Media:
    def __init__(self,t,n,d,i,u,m,c):
        self.type=t
        self.name=n
        self.director=d
        self.imdb_score=i
        self.url=u
        self.duration=m
        self.casts=c


    def showinfo(self):
        if self.type=="film":
            print("the name of film is: ", self.name, "\n director is: ",
            self.director, "\n imdb score is: ", self.imdb_score,
             "\n duration is: ", self.duration, "\n and costs are: ", self.casts)

        elif self.type=="clip":
            print("the name of clip is: ", self.name, "\n director is: ",
            self.director, "\n imdb score is: ", self.imdb_score,
             "\n duration is: ", self.duration, "\n and costs are: ", self.casts)

        elif self.type=="series":
            print("the name of series is: ", self.name, "\n director is: ",
            self.director, "\n imdb score is: ", self.imdb_score,
             "\n duration is: ", self.duration, "\n and costs are: ", self.casts)

        else:
           print("the name of documentary is: ", self.name, "\n director is: ",
            self.director, "\n imdb score is: ", self.imdb_score,
             "\n duration is: ", self.duration, "\n and costs are: ", self.casts)


    def download(self):  
        link=self.url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path="./" , filename="test.mp4")
  