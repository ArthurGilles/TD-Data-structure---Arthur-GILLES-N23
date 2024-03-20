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


f = Fraction(3,4)
print(f)



                 