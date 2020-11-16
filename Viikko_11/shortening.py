import math

class Shortening:
    def __init__(self,n):
        self._edges = []
        self._n = n

    def add_edge(self,a,b,x):
        self._edges.append((a, b, x))

    def check(self,a,b):
        # ajetaan Bellman-Fordia n kierrosta, jos tulos paranee viimeisellä
        #  kierroksella niin polulla on negatiivinen sykli
        for i in range(self._n)

if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(1,3)) # False
    s.add_edge(1,2,5)
    s.add_edge(2,3,-2)
    print(s.check(1,3)) # False
    s.add_edge(2,4,1)
    s.add_edge(4,2,-2)
    print(s.check(1,3)) # True