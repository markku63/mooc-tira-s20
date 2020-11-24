class GraphGame:
    def __init__(self,n):
        self._n = n+1
        self._neighbors = [[] for _ in range(self._n)]
        self._wins = [None]*self._n

    def add_link(self,a,b):
        self._neighbors[a].append(b)
        # ratkaisu muuttunut
        self._wins = [None]*self._n

    def winning(self,x):
        if self._wins[x] != None:
            return self._wins[x]
        else:
            for i in self._neighbors[x]:
                if not self.winning(i):
                    self._wins[x] = True
                    return True
            self._wins[x] = False
            return False


if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3,4)
    g.add_link(1,4)
    g.add_link(4,5)
    print(g.winning(3)) # False
    print(g.winning(1)) # False
    g.add_link(3,1)
    g.add_link(4,6)
    g.add_link(6,5)
    print(g.winning(3)) # True
    print(g.winning(1)) # False
    print(g.winning(2)) # False

    g = GraphGame(10)
    g.add_link(4,1)
    g.add_link(7,6)
    print(g.winning(3))
    g.add_link(5,9)
    print(g.winning(4))
    g.add_link(8,10)
    g.add_link(1,6)
    g.add_link(10,6)
    print(g.winning(10))
    g.add_link(4,1)
    g.add_link(9,4)
    print(g.winning(2))
    g.add_link(2,4)
    g.add_link(4,1)
    g.add_link(5,8)
    print(g.winning(5))
    print(g.winning(4)) # False
    g.add_link(1,6)
    print(g.winning(8))
    print(g.winning(2))