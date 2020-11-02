def count(r):
    # TODO
    reitit = [[0]*len(r[0]) for i in range(len(r))]
    reitit [0][0] = 1
    for y in range(len(r)):
        for x in range(len(r[0])):
            if r[y][x] == "#":
                reitit[y][x] = 0
            elif x != 0 or y != 0:
                reitit[y][x] = reitit[y-1][x] + reitit[y][x-1]
    print(reitit)
    return -1

if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r)) # 2