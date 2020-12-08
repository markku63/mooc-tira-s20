from collections import deque
from math import inf

class Ball:
    def __init__(self,n):
        self._n = n + 3
        self._start = n + 1
        self._end = n + 2
        self._graph = [set() for _ in range(self._n)]
        self._cap = [[0]*self._n for _ in range(self._n)]

    def add_pair(self,a,b):
        self._graph[self._start].add(a)
        self._graph[b].add(self._end)
        self._graph[a].add(b)
        self._cap[a][b] = 1
        self._cap[self._start][a] = 1
        self._cap[b][self._end] = 1

    def _bfs(self, a, b, flows):
        queue = deque()
        parent = [-1]*self._n
        m = [inf]*self._n
        queue.append(a)
        while not len(queue) == 0:
            node = queue.popleft()
            for neighbour in self._graph[node]:
                if self._cap[node][neighbour] - flows[node][neighbour] > 0 and parent[neighbour] == -1:
                    parent[neighbour] = node
                    m[neighbour] = min(m[node], self._cap[node][neighbour] - flows[node][neighbour])
                    if neighbour == b:
                        return m[b], parent
                    queue.append(neighbour)
        return 0, parent

    def calculate(self):
        a = self._n - 2
        b = self._n - 1
        f = 0
        flows = [[0]*self._n for _ in range(self._n)]
        while True:
            m, p = self._bfs(a, b, flows)
            if m == 0:
                return f
            f += m
            v = b
            while v != a:
                u = p[v]
                flows[u][v] += m
                flows[v][u] -= m
                v = u

if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2

    b = Ball(5)
    print(b.calculate())
    b.add_pair(5,5)
    print(b.calculate()) # 1

    b = Ball(5)
    b.add_pair(4,3)
    print(b.calculate())
    b.add_pair(4,1)
    print(b.calculate())
    b.add_pair(2,2)
    print(b.calculate())
    b.add_pair(5,3)
    print(b.calculate())
    print(b.calculate())
    print(b.calculate())
    b.add_pair(1,1)
    print(b.calculate())
    b.add_pair(4,3)
    print(b.calculate())
    print(b.calculate())
    b.add_pair(2,4)
    print(b.calculate()) # 3