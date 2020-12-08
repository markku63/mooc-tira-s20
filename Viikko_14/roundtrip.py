from math import inf
class RoundTrip:
    def __init__(self,n):
        self._n = n
        self._dm = [[inf]*n for _ in range(n)]
        for i in range(n):
            self._dm[i][i] = 0

    def add_route(self,a,b):
        self._dm[a-1][b-1] = 1

    def check(self):
        for k in range(self._n):
            for i in range(self._n):
                for j in range(self._n):
                    self._dm[i][j] = min(self._dm[i][j], self._dm[i][k]+self._dm[k][j])
        return self._dm

if __name__ == "__main__":
    r = RoundTrip(5)
    r.add_route(1,2)
    r.add_route(1,3)
    r.add_route(2,3)
    r.add_route(2,4)
    print(r.check()) # False
    r.add_route(2,5)
    print(r.check()) # False
    r.add_route(3,1)
    print(r.check()) # False
    r.add_route(5,4)
    print(r.check()) # True