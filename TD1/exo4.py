from random import choice
from copy import deepcopy

ALPHABET = [chr(i) for i in range(97, 123)]
ALPHABET.append("?")
POINTS = {
    "?" : 0,
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
    r = [choice(ALPHABET) for i in range(n)]
    while r.count("?") > 1:
        r = [choice(ALPHABET) for i in range(n)]
    return r


def validWords(T):
    r = []
    for w in words:
        ok = True
        left = deepcopy(T)
        for l in w:
            if l not in left:
                if left.count("?") > 0:
                    left.remove("?")
                else:
                    ok = False
                    break
            else:
                left.remove(l)
        if ok:
            r.append(w)
    return r

def score(word,T):
    s = 0
    left = deepcopy(T)
    for l in word:
        if l in left:
            s += POINTS[l]
            left.remove(l)
    return s

def max_score(words):
    solution  = words[0]
    c = score(solution,T)
    for w in W:
        if score(w,T) > c:
            solution = w
            c = score(solution,T)
    print(solution)
    print(score(solution,T))


T = tirage(8)
W = validWords(T)

print(W)
if len(W) == 0:
    print("No words found")
else:
    max_score(W)
    




    


