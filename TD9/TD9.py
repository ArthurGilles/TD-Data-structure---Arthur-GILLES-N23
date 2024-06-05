import unittest
import random

class TestPolynomial(unittest.TestCase):
    """
    Jeu de tests
    """
    def testCreation(self):
        """
        Test les operation de creation et de modulo de la 
        fonction __init__
        """
        P = Polynomial([1,6],4,1)
        self.assertEqual(P,Polynomial([3],4,1))
    
    def testSTR(self):
        # Test __str__
        P = Polynomial([1,6],4,1)
        self.assertEqual(str(P),"3")
    
    def testAdd(self):
        # Test l'addition
        P = Polynomial([1,6,3,3],4,3)
        Q = Polynomial([2,2,1],4,3)
        self.assertEqual(P+Q,Polynomial([0],4,3))

    def testMul(self):
        # Test la multiplication de 2 polynomes
        P = Polynomial([1,6,3,3],4,3)
        Q = Polynomial([0,1],4,3)
        A = P*Q
        self.assertEqual(A,Polynomial([1,2,2],4,3))
    
    def testMul2(self):
        # Test la multiplication par un scalaire
        P = Polynomial([1,6,3,3],4,3)
        A = P * 2
        self.assertEqual(A,Polynomial([0,0,2],4,3))
    
    def testScalar(self):
        # Test la multiplication par un scalaire avec la methode scalar
        P = Polynomial([1,6,3,3],4,3)
        A = P.scalar(2)
        self.assertEqual(A,Polynomial([0,0,2],4,3))
    
    def testRescale(self):
        # Test la fonction rescale
        P = Polynomial([1,6,3,3],4,3)
        A = P.rescale(2)
        self.assertEqual(A,Polynomial([0,0,1],2,3))

class Polynomial:

    def __init__(self,c,q,n):
        """
        Cette methode prend une liste de coefficients c, et deux entiers
        n et q, et cree un polynome, apres avoir fait les operations de
        modulo, afin que le polynome soit dans Z_q/(x^n+1)
        """
        
        self.q = q
        self.n = n
        self.c = c
        # met tous les coef entre 1 et q en faisant un modulo
        self.coefModulo() 
        # Calcule le reste du polynome par x^n+1
        self.polynomialModulo()
        # Comme les coefficients on change, on refait l'operation modulo
        self.coefModulo()

    def coefModulo(self):
        """
        Cette methode met tous les coef entre 1 et q en faisant un
        modulo
        """
        L = []
        for i in self.c:
            L.append(i%self.q)
        self.c = L
    
    def polynomialModulo(self):
        """
        Cette methode change les coefficients, en calculant le reste 
        du polynome par x^n+1
        """
        L = [0]*self.n
        for i in range(len(self.c)):
            if i < self.n:
                L[i] += self.c[i]
            else:
                L[i%self.n] += -self.c[i]
        self.c = L 


    def __add__(self,P):
        # Exercice 2
        """
        Additionne deux polynomes. Comme les operations de modulo sont
        faites automatiquement a la creation d'un polynome, on a pas
        besoin de les faire manuellement dans cette fonction, puisqu'elle
        seront faites dans la fonction __init__ du polynome renvoye
        """
        assert self.q == P.q 
        assert self.n == P.n 
        L = []
        for i in range(len(self.c)):
            L.append(self.c[i]+P.c[i])
        return Polynomial(L,self.q,self.n)

    def __eq__(self,P):
        # Verifie l'egalite d'un polynome avec un autre objet
        if type(P) == type(self) and self.q == P.q and self.n == P.n\
        and self.c == P.c:
            return True
        return False

    def __str__(self):
        s = ""
        for i in range(len(self.c)):
            if self.c[i] != 0:
                if i == 0:
                    s += str(self.c[i])
                else:
                    if self.c[i] == 1:
                        if i == 1:
                            s += f" + X"
                        else:
                            s += f" + X^{i}"
                    elif self.c[i] == -1:
                        if i == 1:
                            s += f" - X"
                        else:
                            s += f" - X^{i}"
                    else:
                        if self.c[i] > 0:
                            s += " + "
                        else:
                            s += " - "
                        if i == 1:
                            s += f"{abs(self.c[i])}X"
                        else:
                            s += f"{abs(self.c[i])}X^{i}"
        if s == "":
            return "0"
        if s[:3] == " + " or s[:3] == " - ":
            return s[3:]
        return s

    def __mul__(self,P):
        # Exercice 3
        """
        Multiplie le polynome avec un autre objet. Si l'objet est un
        polynome, effectue une multiplication de polynome. Sinon, si 
        l'objet est un scalaire, multiplie le polynome par ce scalaire
        """
        if type(P) == type(self): # Multiplie 2 polynomes
            assert P.q == self.q and P.n == self.n
            L = [0]*2*self.n
            for i in range(len(self.c)):
                for j in range(len(P.c)):
                    L[i+j] += self.c[i]*P.c[j]
            return Polynomial(L,self.q,self.n)
        
        elif type(P) == float or type(P) == int:
            # Multiplie avec un scalaire
            L = [P*a for a in self.c]
            return Polynomial(L,self.q,self.n)

    def scalar(self,c):
        # Exercice 4 (1/3)
        """
        La multiplication avec un scalaire a deja ete geree dans la 
        methode __mul__. Il ne reste donc plus qu'a renvoyer le resultat
        de cette multiplication
        """
        return self*c

    def rescale(self,r):
        # Exercice 4 (2/3)
        return Polynomial(self.c,r,self.n)

    
    def fscalar(self,r,a):
        # Exercice 4 (3/3)
        L = [0]*self.n
        for i in range(self.n):
            L[i] = round(self[i]*a)%r
        return Polynomial(L,self.n,self.q)

def gen_uniform_random(q,n,a,b):
    # Exercice 5
    L = []
    for i in range(n):
        L.append(random.randint(a,b))
    return Polynomial(L,q,n)

def chiffrer(b,a,p):
    # Exercice 6
    q = b.q
    t = p.q
    n = b.n
    delta = q%t
    sp = p*delta
    u = gen_uniform_random(q,n,0,1)
    e1 = gen_uniform_random(q,n,-1,1)
    c1 = (b*u) + e1 + sp
    e2 = gen_uniform_random(q,n,-1,1)
    c2 = a*u + e2
    return c1, c2

unittest.main()

        




