import math

class Shortening:
    def __init__(self,n):
        self._edges = []
        self._n = n

    def add_edge(self,a,b,x):
        self._edges.append((a-1, b-1, x))

    def check(self,a,b):
        # ajetaan Bellman-Fordia, jos tulos paranee
        #  kierroksen n-1 jälkeen niin polulla on negatiivinen sykli
        distance = [math.inf]*self._n
        distance[a-1] = 0
        i = 0
        while True:
            i += 1
            changed = False
            b_changed = False
            for edge in self._edges:
                current = distance[edge[1]]
                new = distance[edge[0]] + edge[2]
                if new < current:
                    distance[edge[1]] = new
                    if edge[1] == b-1:
                        b_changed = True
                    changed = True
            # print(distance)
            if not changed: # ei negatiivisia syklejä
                return False
            if i >= self._n and b_changed: # negatiivinen sykli b:hen johtavalla polulla
                return True
            if i > 2*self._n: # negatiivinen sykli jossain muualla kaaviossa
                return False



if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(1,3)) # False
    s.add_edge(1,2,5)
    s.add_edge(2,3,-2)
    print(s.check(1,3)) # False
    s.add_edge(2,4,1)
    s.add_edge(4,2,-2)
    print(s.check(1,3)) # True
