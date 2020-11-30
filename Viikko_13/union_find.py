from random import randrange
from time import perf_counter

class UnionFind():
    def __init__(self, n) -> None:
        self._n = n + 1
        self._vanhempi = [i for i in range(self._n)]
        self._koko = [1]*self._n

    def edustaja(self, x):
        while x != self._vanhempi[x]:
            x = self._vanhempi[x]
        return x
    
    def sama(self, a, b):
        return self.edustaja(a) == self.edustaja(b)

    def yhdista(self, a, b):
        if self.sama(a, b):
            return
        a = self.edustaja(a)
        b = self.edustaja(b)
        if self._koko[a] < self._koko[b]:
            a, b = b, a
        self._vanhempi[b] = a
        self._koko[a] += self._koko[b]
    
    def maara(self):
        return len(set(self._vanhempi[1:]))


if __name__ == "__main__":
    n = 100000
    uf = UnionFind(n)
    alku = perf_counter()
    for _ in range(n):
        a = randrange(1, n)
        b = randrange(1, n)
        uf.yhdista(a, b)
    loppu = perf_counter()
    print("n=", n, "Aikaa kului:", (loppu - alku), " komponenttien määrä:", uf.maara())
