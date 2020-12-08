from collections import deque
from math import inf

class flow():
    def __init__(self, n):
        self._n = n+1
        self._graph = [[] for _ in range(self._n)]
        self._cap = [[0]*self._n for _ in range(self._n)]

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
    
    def add(self, a, b, cap):
        self._graph[a].append(b)
        self._cap[a][b] = cap
    
    def max_flow(self, s, t):
        f = 0
        flows = [[0]*self._n for _ in range(self._n)]
        while True:
            m, p = self._bfs(s, t, flows)
            if m == 0:
                return f
            f += m
            v = t
            while v != s:
                u = p[v]
                flows[u][v] += m
                flows[v][u] -= m
                v = u

f = flow(7)
f.add(1, 2, 7)
f.add(1, 5, 15)
f.add(2, 3, 3)
f.add(2, 4, 2)
f.add(5, 4, 3)
f.add(5, 6, 9)
f.add(4, 3, 4)
f.add(4, 7, 3)
f.add(6, 4, 5)
f.add(6, 7, 5)
f.add(3, 7, 8)
print(f.max_flow(1, 7))

