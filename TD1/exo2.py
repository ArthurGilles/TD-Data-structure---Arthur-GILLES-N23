from random import choice
from copy import deepcopy

ALPHABET = [chr(i) for i in range(97, 123)]

with open("mots.sansaccent.txt","r") as f:
    text = f.read()
words = text.split("\n")


def tirage(n):
    return [choice(ALPHABET) for i in range(n)]

def validWords(T):
    r = []
    for w in words:
        ok = True
        left = deepcopy(T)
        for l in w:
            if l not in left:
                ok = False
                break
            else:
                left.remove(l)
        if ok:
            r.append(w)
    return r

T = tirage(8)

print(T)
W = validWords(T)

print(W)
if len(W) == 0:
    print("No words found")
else:
    solution  = W[0]
    c = len(solution)
    for w in W:
        if len(w) > c:
            solution = w
            c = len(solution)
    print(solution)
    print(len(solution))




    


