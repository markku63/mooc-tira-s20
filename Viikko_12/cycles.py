class Cycles:
    class CycleError(Exception):
        pass

    def __init__(self,n):
        self._neighbours = [[] for _ in range(n+1)]

    def add_edge(self,a,b):
        self._neighbours[a].append(b)

    def _dfs(self, n, visited):
        if visited[n] == 2:
            return
        if visited[n] == 1:
            # solmuun tultu syklin kautta
            raise self.CycleError
        visited[n] = 1
        for i in self._neighbours[n]:
            self._dfs(i, visited)
        visited[n] = 2

    def check(self):
        visited = [0]*len(self._neighbours)
        while True:
            try:
                i = visited.index(0)
            except ValueError:
                # kaikki solmut käsitelty löytämättä syklejä
                return False
            try:
                self._dfs(i, visited)
            except self.CycleError:
                return True

if __name__ == "__main__":
    c = Cycles(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(1,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(4,2)
    print(c.check()) # True