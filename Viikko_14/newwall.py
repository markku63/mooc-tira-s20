from collections import deque
import sys

inf = sys.maxsize

class Maxflow():
    def __init__(self,n):
        self._n = n+1
        self._graph = [[] for _ in range(self._n)]
        self._cap = [[0]*self._n for _ in range(self._n)]

    def add_link(self,a,b,x):
        self._graph[a].append(b)
        self._cap[a][b] += x

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

    def calculate(self,a,b):
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

def count(r):
    n = len(r)
    f = Maxflow(n * n)
    for row in range(n):
        for col in range(n):
            if r[row][col] != '.':
                continue
            if col < n-1 and r[row][col + 1] == '.':
                f.add_link(row * n + col, row * n + col + 1, 1)
            if row < n-1 and r[row+1][col] == '.':
                f.add_link(row * n + col, (row + 1) * n + col, 1)

    return f.calculate(0, n * n - 1)

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2