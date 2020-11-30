class Components:
    def __init__(self, n) -> None:
        self._n = n + 1
        self._vanhempi = [i for i in range(self._n)]
        self._koko = [1]*self._n

    def edustaja(self, x):
        while x != self._vanhempi[x]:
            x = self._vanhempi[x]
        return x

    def add_road(self, a, b):
        a = self.edustaja(a)
        b = self.edustaja(b)
        if a == b:
            return
        if self._koko[a] < self._koko[b]:
            a, b = b, a
        self._vanhempi[b] = a
        self._koko[a] += self._koko[b]
    
    def count(self):
        komponentit = set()
        for i in range(1, self._n):
            komponentit.add(self.edustaja(i))
        return len(komponentit)


if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1,2)
    c.add_road(1,3)
    print(c.count()) # 3
    c.add_road(2,3)
    print(c.count()) # 3
    c.add_road(4,5)
    print(c.count()) # 2
