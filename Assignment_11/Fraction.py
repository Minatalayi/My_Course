import math
class Fraction:
    def __init__(self,ss,mm):
        # properties
        self.s=ss
        if mm != 0:
            self.m = mm
        else:
            self.m = 1

    # methodes

    def add(self,other):
        s=self.s*other.m + self.m*other.s
        m=self.m*other.m
        x=Fraction(s,m)
        return x     
   
    def sub(self,other):
        s=self.s*other.m - self.m*other.s
        m=self.m*other.m
        x=Fraction(s,m)
        return x

    def mul(self,other):
        s=self.s*other.s
        m=self.m*other.m
        x=Fraction(s,m)
        return x
   
    def div(self,other):
        s=self.s*other.m
        m=self.m*other.s
        x=Fraction(s,m)
        return x
   
    def fraction_to_number(self):
        x=self.s/self.m
        return x
   
    def show(self):
        print(self.s, "/", self.m)

    def simplify(self):
        gcd = math.gcd(self.s,self.m)
        s= int(self.s/gcd)
        m= int(self.m/gcd)
        x = Fraction(s,m)
        return x


f1=Fraction(5,7)
f2=Fraction(3,8)

f1.show()
f2.show()

sum_result=f1.add(f2)
sum_result.show()

print(f1.fraction_to_number())
simpled=f1.simplify()
simpled.show()

div_result=f1.div(f2)
div_result.show()