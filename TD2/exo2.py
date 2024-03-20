from math import gcd


class Fraction:
    """
    Class representing a fraction
    """
    def __init__(self,n,d):
        assert d != 0
        assert type(n) == int
        assert type(d) == int 
        self.n = n
        self.d = d

    def __repr__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"

    def add(self,obj):
        self.n = self.n*obj.d+obj.n*self.d 
        self.d = self.d*obj.d

    def mult(self,obj):
        self.n = self.n*obj.n
        self.d = self.d*obj.d
    
    def simplify(self):
        self.n, self.d = int(self.n/gcd(int(self.n),int(self.d))), int(self.d/gcd(int(self.n),int(self.d)))
    
    def decimal(self):
        return self.n/self.d
        
# Tests
# An instance of a fraction is created and set to be equal to 3/4
f = Fraction(3,4)
# 3/4 is added to it, which makes it equal to 3/2
f.add(Fraction(3,4))
f.mult(Fraction(2,1))
# It is multiplied by 2, making it equal to 3
print(f)
# It needs to be simplified, so that it is not represented as 12/4
f.simplify()
print(f)


                 