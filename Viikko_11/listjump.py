import math
from heapq import heappush, heappop

class BestRoute:
    def __init__(self,n):
        self._verkko = [[] for _ in range(n)]
        self._n = n

    def add_jump(self,a,b,x):
        self._verkko[a].append((b, x))

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

def calculate(t):
    r = BestRoute(len(t))
    for i in range(len(t)):
        l = t[i]
        if i - l >= 0:
            r.add_jump(i, i - l, l)
        if i + l < len(t):
            r.add_jump(i, i + l, l)
    return r.find_route(0, len(t) - 1)

if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32