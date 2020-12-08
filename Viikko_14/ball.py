from collections import deque
from typing import Set, Mapping, Tuple
import sys

inf = sys.maxsize

class Ball:
    def __init__(self, n: int) -> None:
        self._graph: Mapping[str, Set[str]] = {}
        self._cap: Mapping[Tuple[str, str], int] = {}
        self._graph["start"] = set()
        self._graph["end"] = set()

    def add_pair(self, a: int, b: int) -> None:
        a: str = "K"+str(a)
        b: str = "V"+str(b)
        if a not in self._graph:
            self._graph[a] = set()
        if b not in self._graph:
            self._graph[b] = set()
        self._graph["start"].add(a)
        self._cap[("start", a)] = 1
        self._graph[b].add("end")
        self._cap[(b, "end")] = 1
        self._graph[a].add(b)
        self._cap[(a, b)] = 1

    def _bfs(self, a: str, b: str, flows: Mapping[Tuple[str, str], int]) -> Tuple[int, Mapping[str, str]]:
        queue = deque()
        parent: Mapping[str, str] = {}
        m: Mapping[str, int] = {a: inf}
        queue.append(a)
        while not len(queue) == 0:
            node = queue.popleft()
            for neighbour in self._graph[node]:
                if self._cap[(node, neighbour)] - flows[(node, neighbour)] > 0 and neighbour not in parent:
                    parent[neighbour] = node
                    m[neighbour] = min(m[node], self._cap[(node, neighbour)] - flows[(node, neighbour)])
                    if neighbour == b:
                        return m[b], parent
                    queue.append(neighbour)
        return 0, parent

    def calculate(self):
        a: str = "start"
        b: str = "end"
        f: int = 0
        flows = dict.fromkeys(self._cap, 0)
        while True:
            m, p = self._bfs(a, b, flows)
            if m == 0:
                return f
            f += m
            v = b
            while v != a:
                u = p[v]
                flows[(u, v)] = flows.get((u, v), 0) + m
                flows[(v, u)] = flows.get((v, u), 0) - m
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
    print(b.calculate())
    b.add_pair(3,4)
    print(b.calculate())
    print(b.calculate())
    print(b.calculate())
    b.add_pair(1,3)
    b.add_pair(4,2)
    print(b.calculate())
    b.add_pair(5,3)
    b.add_pair(5,1)
    b.add_pair(1,4)
    b.add_pair(1,2)
    b.add_pair(1,3)
    print(b.calculate())
    print(b.calculate())
    b.add_pair(4,5)
    print(b.calculate())
    b.add_pair(2,5)
    b.add_pair(5,5)
    print(b.calculate()) # 5