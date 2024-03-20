
class Polynomial:
    """
    Class representing a polynomial
    """
    def __init__(self,c):
        self.c = c

    def __str__(self):
        s = ""
        for i in range(len(self.c)):
            if i == 0:
                s += f"{self.c[i]}"
            else:
                s += f"{self.c[i]}X**{i}"
            
            if i + 1 != len(self.c):
                s += " + "
        return s
    
P = Polynomial([1,2,3,5,8])
print(P)





