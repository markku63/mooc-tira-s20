class MaxSet:
    def __init__(self,n):
        self._n = n + 1
        self._vanhempi = [i for i in range(self._n)]
        self._koko = [1]*self._n
        self._max = 1

    def _edustaja(self, x):
        while x != self._vanhempi[x]:
            x = self._vanhempi[x]
        return x

    def merge(self,a,b):
        a = self._edustaja(a)
        b = self._edustaja(b)
        if a == b:
            return
        if self._koko[a] < self._koko[b]:
            a, b = b, a
        self._vanhempi[b] = a
        self._koko[a] += self._koko[b]
        self._max = max(self._max, self._koko[a])

    def get_max(self):
        return self._max

if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1,2)
    m.merge(3,4)
    m.merge(3,5)
    print(m.get_max()) # 3
    m.merge(1,5)
    print(m.get_max()) # 5