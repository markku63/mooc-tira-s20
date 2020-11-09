def count(r):
    def dfs(r, x, y, visited):
        if y < 0 or x < 0 or y >= len(r) or x >= len(r[0]):
            return
        if visited[y][x] or r[y][x] == "#":
            return
        visited[y][x] = True
        dfs(r, x, y+1, visited)
        dfs(r, x, y-1, visited)
        dfs(r, x+1, y, visited)
        dfs(r, x-1, y, visited)

    m = len(r[0])
    n = len(r)
    visited = [[False]*m for _ in range(n)]
    counter = 0
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and r[y][x] ==".":
                dfs(r, x, y, visited)
                counter += 1
    return counter

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3