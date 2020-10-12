from heapq import heappush, heappop

def find(t, k):
    jono=[]
    x = 0
    for i in range(len(t)-1):
        for j in range(i+1, len(t)):
            heappush(jono, abs(t[i]-t[j]))
    for i in range(k):
        x = heappop(jono)
    return x

if __name__ == "__main__":
    t = [4,1,5,2]
    print(find(t,1)) # 1
    print(find(t,2)) # 1
    print(find(t,3)) # 2
    print(find(t,4)) # 3
    print(find(t,5)) # 3
    print(find(t,6)) # 4