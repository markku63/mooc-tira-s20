from collections import deque

def count(r):
    m = len(r)
    n = len(r[0])
    visited = [[False]*n for _ in range(m)]
    distance = [[-1]*n for _ in range(m)]
    start = ()
    end = ()
    queue = deque()

    for y in range(m):
        for x in range(n):
            if r[y][x] == "A":
                start = (x, y)
            elif r[y][x] == "B":
                end = (x, y)
    
    distance[start[1]][start[0]] = 0
    visited[start[1]][start[0]] = True
    queue.append(start)
    while len(queue) > 0:
        pos = queue.popleft()
        for neighbour in [(pos[0], pos[1]-1), (pos[0], pos[1]+1), (pos[0]-1, pos[1]), (pos[0]+1, pos[1])]:
            if visited[neighbour[1]][neighbour[0]] or r[neighbour[1]][neighbour[0]] == "#":
                continue
            queue.append(neighbour)
            visited[neighbour[1]][neighbour[0]] = True
            distance[neighbour[1]][neighbour[0]] = distance[pos[1]][pos[0]] +1
    return distance[end[1]][end[0]]

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7