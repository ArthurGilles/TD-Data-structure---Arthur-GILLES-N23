import unittest

class TestTree(unittest.TestCase):
    def test_label(self):
        T = Tree("f",Tree("a"),Tree("b"))
        self.assertEqual(T.label(),"f")

    def test_nb_children(self):
        T = Tree("f",Tree("a"),Tree("b"))
        self.assertEqual(T.nb_children(),2)

    def test_child(self):
        T = Tree("f",Tree("a"),Tree("b"))
        self.assertEqual(T.child(1).label(),"b")

    def test_is_leaf(self):
        T = Tree("f",Tree("a"),Tree("b"))
        self.assertEqual(T.is_leaf(),False)

    def test_depth(self):
        T = Tree("f",Tree("a"),Tree("b"))
        self.assertEqual(T.depth(), 1)
        U = Tree("e",Tree("b"),T)
        self.assertEqual(U.depth(),2)

    def test_str(self):
        T = Tree("f",Tree("a"),Tree("b"))        
        U = Tree("e",Tree("b"),T)
        self.assertEqual(str(U),"e(b,f(a,b))")

    def test_eq(self):
        T = Tree("f",Tree("a"),Tree("b"))
        U = Tree("e",Tree("b"),T)
        V = Tree("f",Tree("a"),Tree("b"))
        W = Tree("e",Tree("b"),V)
        self.assertEqual(W,U)
        X = Tree("f",Tree("a"),Tree("c"))
        Y = Tree("e",Tree("b"),V)
        self.assertFalse(X == Y)
        

class Tree:

    def __init__(self,value,*children):
        for i in children:
            assert type(i) == Tree
        self.__value = value
        self.__children = children

    
    def label(self):
        return self.__value
    
    def children(self):
        return self.__children
    
    def nb_children(self):
        return len(self.__children)
    
    def child(self,i):
        return self.__children[i]

    def is_leaf(self):
        if len(self.__children) == 0:
            return True
        return False
    
    def depth(self):
        if self.is_leaf():
            return 0
        return 1 + max([i.depth() for i in self.children()])
    
    def __str__(self):
        if self.is_leaf():
            return str(self.__value)
        s = str(self.__value)+"("
        for c in self.__children: 
            s += str(c) + ","
        return s[:-1] + ")"

    def __eq__(self,obj):
        if len(self.__children) != len(obj.children()):
            return False
        
        if len(self.__children) == 0:
            if self.label() == obj.label():
                return True
            return False
        
        for i in range(len(self.__children)):
            if self.__children[i] != obj.children()[i]:
                return False
        return True 

    def deriv(self):
        # Assuming x to the 4 is written as "X**4"
        if self.label() == "X":
                return Tree("1")
        elif self.label() not in ["+", "*"]:
            return Tree("0")
        
        if self.label() == "+":
            return Tree("+",*[obj.deriv() for obj in self.children()])
        if self.label() == "*":
            return Tree("+",Tree("*",self.children()[0].deriv(),self.children()[1]),Tree("*",self.children()[0],self.children()[1].deriv()))

    def substitute(self,t1,t2):
        if self == t1:
            return t2
        elif self.is_leaf():
            return self
        else:
            return Tree(self.label(),self.children()[0].substitute(t1,t2),self.children()[1].substitute(t1,t2))
    









if __name__ == '__main__':
    print("Test de derivation sur le polynome donne")
    a = Tree("*",Tree("5"),Tree("X"))
    b = Tree("+", Tree("7"),a)
    c = Tree("*",Tree("X"),Tree("X"))
    d = Tree("*",Tree("3"),c)
    T = Tree("+", b,d)
    print("Polynome non derive")
    print(T)
    print("Polynome derive")
    print(T.deriv())
    print("Test de substitution sur le polynome donne")
    print("Polynome non substitue")
    print(a)
    print("Polynome substitue")
    print(Tree('+', Tree('a'), Tree('X')).substitute(Tree('X'), Tree('b')))
    # Test
    unittest.main()
