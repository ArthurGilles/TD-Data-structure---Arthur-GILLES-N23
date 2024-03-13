from random import choice
from copy import deepcopy

ALPHABET = [chr(i) for i in range(97, 123)]
POINTS = {
    'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'd': 2, 'g': 2, 'm': 2,
    'b': 3, 'c': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4,
    'j': 8, 'q': 8,
    'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10
}

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

def score(word):
    s = 0
    for l in word:
        s += POINTS[l]
    return s

def max_score(words):
    solution  = words[0]
    c = score(solution)
    for w in W:
        if score(w) > c:
            solution = w
            c = score(solution)
    print(solution)
    print(score(solution))


T = tirage(8)

print(T)
W = validWords(T)

print(W)
if len(W) == 0:
    print("No words found")
else:
    max_score(W)
    




    


