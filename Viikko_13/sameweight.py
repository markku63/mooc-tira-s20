class UnionFind:
    def __init__(self, n):
        self._n = n + 1
        self._vanhempi = [i for i in range(self._n)]
        self._koko = [1]*self._n

    def _edustaja(self, x):
        while x != self._vanhempi[x]:
            x = self._vanhempi[x]
        return x

    def yhdista(self, a, b):
        a = self._edustaja(a)
        b = self._edustaja(b)
        if a == b:
            return False
        if self._koko[a] < self._koko[b]:
            a, b = b, a
        self._vanhempi[b] = a
        self._koko[a] += self._koko[b]
        return True
    
    def maara(self):
        komponentit = set()
        for i in range(1, self._n):
            komponentit.add(self._edustaja(i))
        return len(komponentit)


class SameWeight:
    def __init__(self,n):
        self._n = n
        self._edges = []

    def add_edge(self,a,b,x):
        self._edges.append((x, (a, b)))

    def cost(self, max=False):
        cost = 0
        uf = UnionFind(self._n)
        for t in sorted(self._edges, reverse=max):
            if uf.yhdista(t[1][0], t[1][1]):
                cost += t[0]
        return cost if uf.maara() == 1 else -1

    def check(self):
        return self.cost(False) == self.cost(True)

if __name__ == "__main__":
    s = SameWeight(4)
    s.add_edge(1,2,2)
    s.add_edge(1,3,3)
    print(s.check()) # True
    s.add_edge(1,4,3)
    print(s.check()) # True
    s.add_edge(3,4,3)
    print(s.check()) # True
    s.add_edge(2,4,1)
    print(s.check()) # False