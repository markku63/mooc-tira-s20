def count_r(r, x, y, n, mem):
    if y >= n or x >= n or r[y][x] == "#": # seinä tai ulkopuoli
        if y< n and x < n:
            mem[y][x] = -1
        return -1
    elif mem[y][x]: # jo käyty ruutu
        return mem[y][x]
    elif x == n-1 and y == n-1: # viimeinen ruutu
        if r[y][x] == "@":
            mem[y][x] = 1
            return 1
        else:
            mem[y][x] = 0
            return 0
    else:
        cur = 1 if r[y][x] == "@" else 0
        right = count_r(r, x+1, y, n, mem)
        down = count_r(r, x, y+1, n, mem)
        res = 0
        if right == -1 and down == -1:
            res = -1
        elif right == -1:
            res = cur + down
        elif down == -1:
            res = cur + right
        else:
            res = cur + min(right, down)
        mem[y][x] = res
        return res
    

def count(r):
    n = len(r)
    mem = [[None]*n for _ in range(n)]
    return count_r(r, 0, 0, n, mem)

def count2(r):
    n = len(r)
    reitit = [[None]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            res = 0
            if r[y][x] == "#":
                res = -1
            elif x==0 and y==0 and r[y][x] == "@":
                res = 1
            else:
                left = reitit[y][x-1] if x > 0 else -1
                up = reitit[y-1][x] if y > 0 else -1
                cur = 1 if r[y][x] == "@" else 0
                if left == -1 and up == -1: # ei reittiä
                    res = -1
                elif left == -1:
                    res = cur + up
                elif up == -1:
                    res = cur + left
                else:
                    res = cur + min(left, up)
            reitit[y][x] = res
    return reitit[n-1][n-1]
                

if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r) == count2(r)) # 2
    r = ["...@.",
         ".....",
         "..#..",
         "..@..",
         "@...@"]
    print(count(r) == count2(r)) # 1
    r = ["@..@#",
         ".@@@@",
         "@.@#@",
         "..#..",
         "@@.@."]
    print(count(r) == count2(r)) # 4
    r = ["#@.@#",
         "@...@",
         "@@@##",
         "@#@@@",
         "@.#@@"]
    print(count(r) == count2(r)) # -1
    r = ["@@@#@",
         ".#@#@",
         ".@#@#",
         "##.@@",
         "#@.@@"]
    print(count(r) == count2(r)) # -1