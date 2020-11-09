class Cities:
    def __init__(self,n):
        self._n = n + 1
        self._neighbours = [[] for _ in range(self._n)]

    def add_road(self,a,b):
        self._neighbours[a].append(b)
        self._neighbours[b].append(a)


    def has_route(self,a,b):
        visited = [False]*self._n
        return self._dfs(a, b, visited)

    def _dfs(self, a, b, visited):
        if a ==b:
            return True
        if visited[a]:
            return False
        visited[a] = True
        for n in self._neighbours[a]:
            if self._dfs(n, b, visited):
                return True
        return False

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True