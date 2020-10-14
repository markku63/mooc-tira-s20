from heapq import heappush, heappop, nsmallest

def find(t, k):
    return nsmallest(k, (abs(t[i] - t[j]) for i in range(len(t) - 1) for j in range(i + 1, len(t))))[k - 1]

if __name__ == "__main__":
    t = [4,1,5,2]
    print(find(t,1)) # 1
    print(find(t,2)) # 1
    print(find(t,3)) # 2
    print(find(t,4)) # 3
    print(find(t,5)) # 3
    print(find(t,6)) # 4

    t = [9, 6, 10, 3, 7, 5]
    print(find(t, 7)) # 3