class Connectivity:
    def __init__(self,n):
        self._n = n + 1
        self._vanhempi = [i for i in range(self._n)]
        self._koko = [1]*self._n

    def _edustaja(self, x):
        while x != self._vanhempi[x]:
            x = self._vanhempi[x]
        return x


    def add_edge(self,a,b):
        a = self._edustaja(a)
        b = self._edustaja(b)
        if a == b:
            return
        if self._koko[a] < self._koko[b]:
            a, b = b, a
        self._vanhempi[b] = a
        self._koko[a] += self._koko[b]

    def count(self):
        komponentit = set()
        for i in range(1, self._n):
            komponentit.add(self._edustaja(i))
        return len(komponentit) - 1

if __name__ == "__main__":
    c = Connectivity(5)
    print(c.count()) # 4
    c.add_edge(2,4)
    c.add_edge(3,5)
    print(c.count()) # 2
    c.add_edge(2,3)
    c.add_edge(3,4)
    print(c.count()) # 1
    c.add_edge(1,2)
    print(c.count()) # 0