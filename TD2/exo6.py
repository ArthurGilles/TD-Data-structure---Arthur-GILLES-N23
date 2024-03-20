
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
                if self.c[i] != 1:
                    s += f"{self.c[i]}X**{i}"
                else:
                    s += f"X**{i}"
            
            if i + 1 != len(self.c):
                s += " + "
        return s
    
    def add(self,obj):
        L = []
        i = 0
        while True:
            if i < len(self.c) and i < len(obj.c):
                L.append(self.c[i]+obj.c[i])
            elif i < len(self.c):
                L.append(self.c[i])
            elif i < len(self.c):
                L.append(obj.c[i])
            else:
                break
            i += 1
        self.c = L
    
    def deriv(self):
        L = []
        for i in range(1,len(self.c)):
            L.append(i*self.c[i])
        self.c = L

    def integrate(self,K):
        L = [K]
        for i in range(len(self.c)):
            L.append(self.c[i]/(i+1))
        self.c = L

P = Polynomial([1,2,3,5,8])
print("Originial polynomial : ")
print(P)
print() # Printing another line to make it look nicer


P = Polynomial([1,2,3,5,8])
Q = Polynomial([1,2,3,5,8])
P.add(Q)
print("Addition : ")
print(P)
print()



P = Polynomial([1,2,3,5,8])
P.deriv()
print("Differentiate")
print(P)
print()

P = Polynomial([1,2,3,5,8])
P.integrate(100)
print("Integrate : ")
print(P)
print()
