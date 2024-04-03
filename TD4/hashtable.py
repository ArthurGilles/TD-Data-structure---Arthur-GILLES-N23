import matplotlib.pyplot as plt
import random
import time

class Hashtable:

    def __init__(self,hash,N=1000):
        self.hash = hash
        self.N = N
        self.elements = 0 # Number of elements in the hash table
        self.array = [[] for i in range(N)]
    
    def put(self,key,value):
        t0 = time.perf_counter()
        h = self.hash(key) % self.N
        for i in range(len(self.array[h])):
            if self.array[h][i][0] == key:
                self.elements -= 1
                del self.array[h][i]
                break
        self.array[h].append((key,value))
        self.elements += 1
        if self.elements > self.N * 1.2:
            self.resize(2*self.N)
        print(f"Time elapsed : {time.perf_counter() - t0}") 

    def get(self,key):
        t0 = time.perf_counter()
        h = self.hash(key) % self.N
        for i in self.array[h]:
            if i[0] == key:
                print(f"Time elapsed : {time.perf_counter() - t0}") 
                return i[1]
        print(f"Time elapsed : {time.perf_counter() - t0}") 
        return None

    def repartition(self):
        y = [len(i) for i in self.array]
        x = [i for i in range(self.N)]
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

    def resize(self,N):
        array = [[] for i in range(N)]
        for i in self.array:
            for j in i:
                key = j[0]
                value = j[1]
                h = self.hash(key) % N
                array[h].append((key,value))

    def __setitem__(self,key,value):
        h = self.hash(key) % self.N
        for i in range(len(self.array[h])):
            if self.array[h][i][0] == key:
                self.elements -= 1
                del self.array[h][i]
                break
        self.array[h].append((key,value))
        self.elements += 1
        if self.elements > self.N * 1.2:
            self.resize(2*self.N)
    
    def __getitem__(self,key):
        h = self.hash(key) % self.N
        for i in self.array[h]:
            if i[0] == key:
                return i[1]
        raise KeyError(f"{str(key)} does not exist")


def naivehash(s):
    return sum([ord(i) for i in s])

def hash(s):
    h = 0
    for i in s:
        h = 31*h + ord(i)
    return h

def wordLength():
    with open("frenchssaccent.dic","r") as f:
        text = f.read()
        words = text.split("\n")[:10000]
    hs = Hashtable(naivehash,N=300)
    for w in words:
        hs.put(w,len(w))
    hs.repartition()



## Test 1
print(naivehash("abc"))

## Test 2
D = Hashtable(naivehash)
D.put("abc",3)

## Test 3
print(D.get("aaa"))
print(D.get("abc"))

## Test 4
"""
hs = Hashtable(naivehash)
for i in range(2000):
    s = ""
    while random.random() < 0.3:
        pass
"""
## Test 5
#wordLength()

## Test 6
D = Hashtable(hash)
D.put("abc",3)
D.resize(2000)

## Test 891239
D = Hashtable(hash)
D["XXX"] = 9 
print(D["XXX"])