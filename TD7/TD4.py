from tkinter import Tk, Canvas,Button,TOP,BOTTOM,LEFT,RIGHT,Label
import random
from copy import deepcopy

WIDTH = 600        # Width of the window
HEIGHT = 600       # Height of the window
R = 10             # Radius of the nodes
P = 0.4            # Probability to create a path with adjacent node
Nline = int(WIDTH/(3*R)-1) # Number of nodes per line
Ncol = int(HEIGHT/(3*R)-1) # Number of nodes per column


class graphGUI:
    """
    This class creates the graphical user interface
    """
    def __init__(self,graph,pos,colIndex):
        # In this function, the window and the canva are created
        self.graph = graph
        self.pos = pos
        self.colIndex = colIndex

        self.root = Tk()
        self.root.title("Graph")
        self.canvas = Canvas(self.root, bg='white', height=HEIGHT, width=WIDTH)
        self.canvas.pack(side=TOP)

        self.draw(graph,pos)
        self.root.mainloop()

    
    def draw(self, graph, pos):
        # This function is used to display the graph on the canva
        self.canvas.delete("all")
        for i in range(len(graph)):
            for j in graph[i]:  # sucs from i to j
                self.canvas.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
        for i in range(len(pos)):
            x, y = pos[i]
            self.canvas.create_oval(x-R,y-R,x+R,y+R,fill=COLORS[self.colIndex[i]])
            self.canvas.create_text(x,y,text=f"{i}")

def makeGrid():
    """
    Creates a random Nlines*Ncolumn random graph, and the positions
    associated to each node and returns them 
    """
    graph = []
    pos = []
    for i in range(Nline):
        for j in range(Ncol):
            pos.append([2*R+3*j*R,2*R+3*i*R])
            N = []
            if j != Ncol-1 and random.random() > 1-P:
                N.append(i*Nline+j+1)
            if i != Nline - 1 and random.random() > 1-P:
                N.append((i+1)*Nline+j)
            graph.append(N)
    return graph,pos

def color_generator():
    r, g, b = random.randint(0,255), random.randint(0,255),random.randint(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"

def neighbors(i,graph):
    # Computes the list of neighbors of a node i in a graph
    L = deepcopy(graph[i])
    if i not in L:
        L.append(i)
    for j in range(len(graph)):
        if i == j:
            continue
        if i in graph[j] and j not in L:
            L.append(j)
    return L

def minLocal(i,graph,color):
    # Finds the local minimum of a node i in a graph and returns it
    return min([color[j] for j in neighbors(i,graph)])

def changeColor(i,graph,colIndex):
    # Sets the color of all neighbors to the one of the local minimum of i 
    minCol = minLocal(i,graph,colIndex)
    N = neighbors(i,graph)
    for j in N:
            if colIndex[j] != minCol:
                # If the of a node color is changed, calls the function
                # on it again, in order to avoid some nodes not to be colored
                colIndex[j] = minCol
                changeColor(j,graph,colIndex)
            

def colorConnex(graph):
    # Goes through the list of all nodes and changes their color
    colIndex = [i for i in range(len(graph))]
    for i in range(len(graph)):
        changeColor(i,graph,colIndex)
    return colIndex

def test(graph,colIndex):
    # Tests if the connex components all have been detected properly
    for node in range(len(graph)):
        N = neighbors(node,graph)
        for j in N:
            if colIndex[node] != colIndex[j]:
                print(node,j)
                return False
    return True

if __name__ == "__main__":
    COLORS = [color_generator() for i in range((Nline+2)*(Ncol+2))]
    graph,pos = makeGrid()
    colIndex = colorConnex(graph)
    graphGUI(graph,pos,colIndex)

