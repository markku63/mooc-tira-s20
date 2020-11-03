import sys

def count(r):
    if r[0][0] == "#":
        return -1
    n = len(r)
    reitit = [[0]*(n+1) for i in range(n+1)]
    for i in range(len(reitit)):
        reitit[0][i] = sys.maxsize
        reitit[i][0] = sys.maxsize
    
    for y in range(1, n+1):
        for x in range(1, n+1):
            if r[y-1][x-1] == "#":
                reitit[y][x] = sys.maxsize
            elif r[y-1][x-1] == "@":
                prev = min(reitit[y-1][x], reitit[y][x-1])
                reitit[y][x] =  prev + 1 if prev < sys.maxsize else 1
            elif x == 1 or y == 1:
                prev = min(reitit[y-1][x], reitit[y][x-1])
                reitit[y][x] = prev if prev < sys.maxsize else 0
            else:
                reitit[y][x] = min(reitit[y-1][x], reitit[y][x-1])
    return reitit[n][n] if reitit[n][n] < sys.maxsize else -1

if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r)) # 2
    r = ["...@.",
         ".....",
         "..#..",
         "..@..",
         "@...@"]
    print(count(r)) # 1
    r = ["@..@#",
         ".@@@@",
         "@.@#@",
         "..#..",
         "@@.@."]
    print(count(r)) # 4
    r = ["#@.@#",
         "@...@",
         "@@@##",
         "@#@@@",
         "@.#@@"]
    print(count(r)) # -1
    r = ["@@@#@",
         ".#@#@",
         ".@#@#",
         "##.@@",
         "#@.@@"]
    print(count(r)) # -1