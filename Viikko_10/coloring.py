class Coloring:
    def __init__(self,n):
        self._n = n + 1
        self._neighbours = [[] for _ in range(self._n)]

    def add_edge(self,a,b):
        self._neighbours[a].append(b)
        self._neighbours[b].append(a)

    def check(self):
        for i in range(self._n):
            if len(self._neighbours[i]) != 0:
                visited = [False]*self._n
                colours = [None]*self._n
                visited[i] = True
                colours[i] = True
                if not self._dfs(i, visited, colours):
                    return False
        return True
    
    def _dfs(self, node, visited, colours):
        for neighbour in self._neighbours[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                colours[neighbour] = not colours[node]
                if not self._dfs(neighbour, visited, colours):
                    return False
            elif colours[node] == colours[neighbour]:
                return False
        return True


if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False

    c = Coloring(5)
    print(c.check())
    print(c.check())
    c.add_edge(1,5)
    c.add_edge(2,4)
    print(c.check())
    c.add_edge(3,4)
    c.add_edge(2,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(3,5)