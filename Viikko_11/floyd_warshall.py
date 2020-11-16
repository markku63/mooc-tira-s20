import math
from random import randint, randrange
from time import perf_counter

n = 1000
m = 10*n
kaaret = []
etaisyys = [[math.inf]*n for _ in range(n)]
for i in range(n):
    etaisyys[i][i] = 0
kierrokset = 0

for i in range(m):
    alku = randrange(n)
    while True:
        loppu = randrange(n)
        if loppu != alku:
            break
    paino = randint(1, 100)
    kaaret.append((alku, loppu, paino))
    etaisyys[alku][loppu] = paino

aloitus = perf_counter()
for k in range(n):
    for i in range(n):
        for j in range(n):
            etaisyys[i][j] = min(etaisyys[i][j], etaisyys[i][k]+etaisyys[k][j])
lopetus = perf_counter()

print("aikaa kului:", (lopetus - aloitus))