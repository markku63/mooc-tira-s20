import math
from random import randint, randrange
from time import perf_counter

n = 100000
m = 10*n
kaaret = []
etaisyys = [math.inf]*n
etaisyys[0] = 0
kierrokset = 0

for i in range(m):
    alku = randrange(n)
    loppu = randrange(n)
    paino = randint(1, 100)
    kaaret.append((alku, loppu, paino))

aloitus = perf_counter()
while True:
    muutos = False
    for kaari in kaaret:
        nyky = etaisyys[kaari[1]]
        uusi = etaisyys[kaari[0]] + kaari[2]
        if uusi < nyky:
            etaisyys[kaari[1]] = uusi
            muutos = True
    kierrokset += 1
    if not muutos:
        break
lopetus = perf_counter()

print("kierroksia:", kierrokset)
print("aika:", (lopetus - aloitus))