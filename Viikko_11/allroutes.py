import math
import copy

class AllRoutes:
    def __init__(self,n):
        self._dist = [[math.inf]*n for _ in range(n)]
        for i in range(n):
            self._dist[i][i] = 0
        self._n = n

    def add_road(self,a,b,x):
        if x < self._dist[a-1][b-1]:
            self._dist[a-1][b-1] = x
            self._dist[b-1][a-1] = x

    def get_table(self):
        for k in range(self._n):
            for i in range(self._n):
                for j in range(self._n):
                    newdist = min(self._dist[i][j],
                                            self._dist[i][k] + self._dist[k][j])
                    self._dist[i][j] = newdist
                    self._dist[j][i] = newdist
        res = copy.deepcopy(self._dist)
        for y in range(len(res)):
            for x in range(len(res[y])):
                if math.isinf(res[y][x]):
                    res[y][x] = -1
        return res

if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1,2,2)
    a.add_road(1,3,5)
    a.add_road(2,3,1)
    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]

    b = AllRoutes(5)
    b.add_road(3,4,6)
    b.add_road(4,5,5)
    b.add_road(4,5,6)
    b.add_road(1,5,7)
    b.add_road(1,4,7)
    b.add_road(4,5,1)
    b.add_road(3,4,8)
    b.add_road(2,3,6)
    b.add_road(4,5,4)
    print(b.get_table())
    # [[0, 19, 13, 7, 7], [19, 0, 6, 12, 13], [13, 6, 0, 6, 7], [7, 12, 6, 0, 1], [7, 13, 7, 1, 0]]