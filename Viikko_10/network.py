from collections import deque

class Network:
    def __init__(self,n):
        self._n = n + 1
        self._neighbours = [[] for _ in range(self._n)]

    def add_link(self,a,b):
        self._neighbours[a].append(b)
        self._neighbours[b].append(a)

    def best_route(self,a,b):
        queue = deque()
        visited = [False]*self._n
        distance = [-1]*self._n
        distance[a] = 0
        queue.append(a)
        visited[a] = True
        while not len(queue) == 0:
            node = queue.popleft()
            for neighbour in self._neighbours[node]:
                if visited[neighbour]:
                    continue
                queue.append(neighbour)
                visited[neighbour] = True
                distance[neighbour] = distance[node] + 1
        return distance[b]

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2