def count(r):
    n = len(r)
    reitit = [[None]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            res = 0
            if r[y][x] == "#":
                res = -1
            elif x==0 and y==0:
                res = 1 if r[y][x] == "@" else 0
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
    print(count(r)) # 2