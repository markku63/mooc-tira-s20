class WallGrid:
    def __init__(self,n):
        self._n = n
        self._grid =[[False]*n for _ in range(n)]
        self._rooms = 0
        self._parent = {}
        self._size = {}

    def _repr(self, sq):
        while sq != self._parent[sq]:
            # https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf sivu 29
            self._parent[sq] = self._parent[self._parent[sq]]
            sq = self._parent[sq]
        return sq
    
    def _union(self, a, b):
        a = self._repr(a)
        b = self._repr(b)
        if a == b:
            return
        if self._size[a] < self._size[b]:
            a, b = b, a
        self._parent[b] = a
        self._size[a] += self._size[b]

    def remove(self,x,y):
        x, y = x-1, y-1
        # ei tehdä mitään jos seinä jo poistettu
        if not self._grid[y][x]:
            self._grid[y][x] = True
            if (x,y) not in self._parent:
                self._parent[(x,y)] = (x,y)
                self._size[(x,y)] = 1
            for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
                if self._grid[y+dir[0]][x+dir[1]]:
                    self._union((x, y), (x+dir[1], y+dir[0]))
            rooms = set()
            for room in self._parent.keys():
                rooms.add(self._repr(room))
            self._rooms = len(rooms)

    def count(self):
        return self._rooms

if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2,2)
    w.remove(4,2)
    print(w.count()) # 2
    w.remove(3,2)
    print(w.count()) # 1
    w.remove(2,4)
    w.remove(2,4)
    w.remove(4,4)
    print(w.count()) # 3
    w.remove(3,3)
    print(w.count()) # 3
    w.remove(3,4)
    print(w.count()) # 1


    w = WallGrid(72)
    w.remove(69,31)
    print(w.count())
    w.remove(3,65)
    w.remove(23,41)
    print(w.count())
    w.remove(15,46)
    print(w.count())
    w.remove(66,31)
    w.remove(55,62)
    w.remove(34,41)
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(25,39)
    print(w.count())
    w.remove(14,17)
    w.remove(9,7)
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(64,28)
    print(w.count())
    print(w.count())
    w.remove(54,61)
    print(w.count())
    w.remove(57,67)
    w.remove(24,51)
    print(w.count())
    print(w.count())
    w.remove(12,20)
    w.remove(11,37)
    print(w.count())
    print(w.count())
    w.remove(17,52)
    w.remove(10,15)
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(57,65)
    w.remove(39,45)
    w.remove(54,20)
    print(w.count())
    w.remove(20,54)
    print(w.count())
    w.remove(24,22)
    print(w.count())
    w.remove(33,29)
    w.remove(62,38)
    w.remove(51,26)
    print(w.count())