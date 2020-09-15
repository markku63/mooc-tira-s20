from random import shuffle
from time import perf_counter

def isort(taulu):
    for i in range(1, len(taulu)):
        j = i - 1
        while j >= 0 and taulu[j] > taulu[j+1]:
            tmp = taulu[j]
            taulu[j] = taulu[j+1]
            taulu[j+1] = tmp
            j -= 1

n = 10 ** 5
taulu = [0]*n
for i in range(n):
    taulu[i] = i + 1
shuffle(taulu)
alku = perf_counter()
isort(taulu)
loppu = perf_counter()
print("Aikaa kului :",loppu - alku," sekuntia")