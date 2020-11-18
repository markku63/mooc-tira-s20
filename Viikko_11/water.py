import math
from heapq import heappush, heappop

def count(a,b,x):
    # https://en.wikipedia.org/wiki/Water_pouring_puzzle
    # https://www.youtube.com/watch?v=0Oef3MHYEC0
    # https://webpages.uncc.edu/~hbreiter/Exotic/Decanting.pdf

    # kaikki mitattavissa olevat määrät ovat tämän monikertoja
    pienin = math.gcd(a, b)

    # onko ratkaisu yleensä mahdollinen?
    if x % pienin != 0:
        return -1

    # luodaan mahdolliset tilat
    tilat = [(i, j) for i in range(0, a+1, pienin) for j in range(0, b+1, pienin) if i==0 or i==a or j==0 or j==b]
    
    # sallitut siirtymät
    verkko = {t: [] for t in tilat}
    for alku in tilat:
        for loppu in tilat:
            if alku == loppu:
                continue
            if alku[0] == loppu[0] and (loppu[1] == 0 or loppu[1] == b):
                # 1. astia pysyy samana, 2. täyttyy tai tyhjentyy
                verkko[alku].append((loppu, abs(loppu[1] -  alku[1])))
            elif alku[1] == loppu[1] and (loppu[0] == 0 or loppu[0] == a):
                # 2. astia pysyy samana, 1. täyttyy tai tyhjentyy
                verkko[alku].append((loppu, abs(loppu[0] -  alku[0])))
            elif alku[0] + alku[1] == loppu[0] + loppu[1]:
                # siirto astiasta toiseen, kokonaismäärä säilyy
                verkko[alku].append((loppu, abs(loppu[0] - alku[0])))

    # Dijkstra
    keko = []
    kasitelty = {t: False for t in tilat}
    etaisyys = {t: math.inf for t in tilat}
    etaisyys[(0, 0)] = 0 # lähdetään tilanteesta jossa molemmat astiat tyhjiä
    heappush(keko, (0, (0,0)))
    while len(keko) != 0:
        solmu = heappop(keko)[1]
        if kasitelty[solmu]:
            continue
        kasitelty[solmu] = True
        for kaari in verkko[solmu]:
            nyky = etaisyys[kaari[0]]
            uusi = etaisyys[solmu] + kaari[1]
            if uusi < nyky:
                etaisyys[kaari[0]] = uusi
                heappush(keko, (uusi, kaari[0]))
    
    return min(etaisyys[(x, 0)], etaisyys[(x, b)])



if __name__ == "__main__":
    print(count(5,4,2)) # 22
    print(count(4,3,2)) # 16
    print(count(3,3,1)) # -1
    print(count(10,9,8)) # 46
    print(count(123,456,42)) # 10530