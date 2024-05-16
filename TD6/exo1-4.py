from tkinter import Tk, Canvas,TOP
import numpy as np
from random import random
from copy import deepcopy

WIDTH = 400        # Width of the window
HEIGHT = 400       # Height of the window
R = 9              # Radius of the nodes
dt = 0.005         # Time step 
N = 50             # Number of steps per pressing
alpha = 0.05       # Friction coefficient

class Node:
    """
    Class that represents a node of the graph, containing:
    - Its position (x,y)
    - Its speed (v)
    - The forces applied to it (F)
    - Its successors, in a list of the form:
    [(N0,L0,k0),(N1,L1,k1),...], with Nj the node to which it is
    connected, Lj the initial length of the spring between the node
    "self" and Nj, and kj its stifness
    """

    def __init__(self,x,y,sucs=[],m=1):
        self.m = 1 # mass of the Node
        self.x = x
        self.y = y
        self.v = np.array([0,0],dtype="float64")
        self.F = np.array([0,0],dtype="float64")
        # Contains tuples (N, L, k)
        self.sucs = deepcopy(sucs)

    def randomMove(self,d):
        self.x += (random()*2-1)*d
        self.y += (random()*2-1)*d

    def calculateForce(self):
        """ 
        Function that calculates the forces applied to the Node
        """

        self.F -= self.v*alpha # Adding friction
        # Calculating the spring force
        for c in self.sucs:
            s = c[0]
            L = c[1]
            k = c[2]
            OM = np.array([self.x,self.y])
            ON = np.array([s.x,s.y])
            centre = (OM+ON)/2
            v = OM-centre
            attractionPoint = centre + v/np.linalg.norm(v)*L/2
            self.F += -k*(OM - attractionPoint)
        
    def applyForce(self):
        """
        This function modifies the speed and position of the node 
        according to the forces applied to it
        """
        self.v += self.F/self.m*dt
        if self.x + self.v[0]*dt > WIDTH or self.x+self.v[0]*dt<0:
            self.v[0] *= -1 # Handles the bouncing off the walls
        else:
            self.x += self.v[0]*dt
        if self.y + self.v[1]*dt > HEIGHT or self.y+self.v[1]*dt<0:
            self.v[1] *= -1 # Handles the bouncing off the walls
        else:
            self.y += self.v[1]*dt
        self.F[0] = 0
        self.F[1] = 0
    
    def __repr__(self):
        return f"||{self.x},{self.y}||"

def fPressed(L,g,can):
    for i in range(N):
        can.delete("all")
        for node in L:
            node.calculateForce()
        for node in L:
            node.applyForce()
        for node in L:
            can.create_oval(node.x-R,node.y-R,node.x+R,node.y+R,fill="red")
        for i in range(len(L)):
            for j in range(len(L)):
                if j >= i:
                    continue
                if j in g[i]:
                    can.create_line(L[i].x, L[i].y, L[j].x, L[j].y)

def connectNodes(L,g):
    # Connects the nodes to each other
    assert len(L) == len(g)
    for i in range(len(L)):
        for j in g[i]:
            norm = pow(pow(L[i].x-L[j].x,2)+pow(L[i].y-L[j].y,2),1/2)
            L[i].sucs.append((L[j],norm,1))

def createNodeList(g):
    L = []
    for i in range(len(g)):
        # Creates a list of nodes with random positions and speed
        N = Node(random()*WIDTH,random()*HEIGHT)
        N.v[0] = (random()-0.5)*100
        N.v[1] = (random()-0.5)*100
        L.append(N)
    connectNodes(L,g) # Binds the nodes together
    return L


if __name__ == "__main__":
    """
    The program works the following way : given a graph, represented 
    by a list of successors, a list of Nodes is created (function 
    createNodeList), with initial positions and speed chosen randomly.
    Then, the nodes are bound with each other (function connectNodes).
    Then, whenever f is pressed, the different forces are calculated
    and applied to every node, and all the nodes and bindings are
    displayed (function fPressed)
    """
    root = Tk()
    root.title("Graph")
    canvas = Canvas(root, bg='white', height=HEIGHT, width=WIDTH)
    canvas.pack(side=TOP)

    g = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
    [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
    L = createNodeList(g)
    fPressed(L,g,canvas)
    root.bind("<f>",lambda e:fPressed(L,g,canvas))
    root.mainloop()
