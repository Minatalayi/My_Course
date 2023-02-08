class complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image

    def show(self):
        print(self.real, "+", "i", self.image)

    def sum(self,other):
        new_real=self.real+other.real
        new_image=self.image+other.image
        result=complex(new_real,new_image) 
        return result

    def sub(self,other):
        new_real=self.real-other.real
        new_image=self.image-other.image
        result=complex(new_real,new_image) 
        return result

    def mul(self,other):
        new_real=self.real*other.real-self.image*other.image
        new_image=self.real*other.real+self.image*other.image
        result=complex(new_real,new_image)
        return result

a=complex(8,5)
a.show()  

b=complex(3,9)
b.show()

x=a.sum(b)
x.show()

z=b.sub(a)
z.show()

y=a.mul(b)
y.show()
