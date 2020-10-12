from heapq import heappush, heappop

def smallest(n):
    jono = []
    heappush(jono, 1)
    for i in range(n):
        x = heappop(jono)
        heappush(jono, 2*x)
        heappush(jono, 3*x)
    return heappop(jono)


if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552