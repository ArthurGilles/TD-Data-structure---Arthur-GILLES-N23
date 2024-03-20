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
        

def L(n):
    """
    Function calculating L
    """
    s = Fraction(0,1)
    for i in range(0,n+1):
        s.add(Fraction((-1)**i,2*i+1))
        s.simplify()
    return s

a = L(10000)
print(a)
# Printing the decimal value of H(n)
print(a.decimal())


                 