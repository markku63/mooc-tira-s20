from collections import deque
from typing import List
import sys

inf = sys.maxsize

class Ball:
    def __init__(self, n: int) -> None:
        self._n = n
        self._graph = [[0]*(2*n + 2) for _ in range(2*n + 2)]
        self._seen = None
        self._flow = None

    def add_pair(self, a: int, b: int) -> None:
        self._graph[a][b + self._n] = 1
        self._graph[0][a] = 1
        self._graph[b + self._n][-1] = 1

    def _bfs(self, a: int, b: int, flow: int) -> int:
        if self._seen[a]:
            return 0
        self._seen[a] = True
        if a == b:
            return flow
        for x in range(len(self._graph)):
            if self._flow[a][x] > 0:
                inc = self._bfs(x, b, min(flow, self._flow[a][x]))
                if inc > 0:
                    self._flow[a][x] -= inc
                    self._flow[x][a] += inc
                    return inc
        return 0

    def calculate(self):
        self._flow = [row[:] for row in self._graph]
        total = 0
        while True:
            self._seen = [False]*len(self._graph)
            add = self._bfs(0, len(self._graph)-1, inf)
            if add == 0:
                return total
            total += add


if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2
