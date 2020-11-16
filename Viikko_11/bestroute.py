import math
from heapq import heappush, heappop

class BestRoute:
    def __init__(self,n):
        self._verkko = [[] for _ in range(n + 1)]
        self._n = n + 1

    def add_road(self,a,b,x):
        self._verkko[a].append((b, x))
        self._verkko[b].append((a, x))

    def find_route(self,a,b):
        keko = []
        kasitelty = [False]*self._n
        etaisyys = [math.inf]*self._n
        etaisyys[a] = 0
        heappush(keko, (0, a))
        while len(keko) != 0:
            solmu = heappop(keko)[1]
            if kasitelty[solmu]:
                continue
            kasitelty[solmu] = True
            for kaari in self._verkko[solmu]:
                nyky = etaisyys[kaari[0]]
                uusi = etaisyys[solmu] + kaari[1]
                if uusi < nyky:
                    etaisyys[kaari[0]] = uusi
                    heappush(keko, (uusi, kaari[0]))
        return etaisyys[b] if math.isfinite(etaisyys[b]) else -1

if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3