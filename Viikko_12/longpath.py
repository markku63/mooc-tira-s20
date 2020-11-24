class LongPath:
    def __init__(self,n):
        self._n = n+1
        self._neighbors = [[] for _ in range(self._n)]
        self._predecessors = [[] for _ in range(self._n)]

    def add_edge(self,a,b):
        if b > a:
            self._neighbors[a].append(b)
            self._predecessors[b].append(a)
        else:
            self._neighbors[b].append(a)
            self._predecessors[a].append(b)

    def _dfs(self, node, visited, sorted):
        if visited[node] == 2:
            return
        elif visited[node] == 1:
            # ei ole DAG
            raise ValueError
        else:
            visited[node] = 1
            for i in self._neighbors[node]:
                self._dfs(i, visited, sorted)
            visited[node] = 2
            sorted.append(node)

    def calculate(self):
        # https://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/Docs/longest-path-in-dag.pdf
        # 1. topologinen järjestys
        sorted = []
        visited = [0]*self._n
        for i in range(1, self._n):
            if visited[i] == 0:
                self._dfs(i, visited, sorted)
        sorted.reverse()
        
        # 2. lasketaan pisin polku jokaiseen solmuun
        distances = [0]*self._n
        for v in sorted:
            if len(self._predecessors[v]) > 0:
                distances[v] = max([distances[i] + 1 for i in self._predecessors[v]])
        
        # 3. palautetaan pisin kaikista poluista
        return max(distances)


if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3