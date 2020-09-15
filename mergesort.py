from random import shuffle
from time import perf_counter

def lomita(a1, b1, a2, b2):
    global taulu, apu
    a = a1
    b = b2 + 1
    for i in range(a, b):
        if a2 > b2 or (a1 <= b1 and taulu[a1] <= taulu[a2]):
            apu[i] = taulu[a1]
            a1 += 1
        else:
            apu[i] = taulu[a2]
            a2 += 1
    for i in range(a, b):
        taulu[i] = apu[i]

def jarjesta(a, b):
    if a == b:
        return
    k = (a + b)//2
    jarjesta(a, k)
    jarjesta(k+1, b)
    lomita(a, k, k+1, b)

n = 10 ** 3
taulu = [0]*n
apu = [0]*n
for i in range(n):
    taulu[i] = i + 1
shuffle(taulu)
alku = perf_counter()
jarjesta(0, len(taulu) - 1)
loppu = perf_counter()
print("Aikaa kului :",loppu - alku," sekuntia")