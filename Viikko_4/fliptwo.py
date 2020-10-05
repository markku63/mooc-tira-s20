from collections import deque

def solve(n,k):
    pakka = deque([i+1 for i in range(n)])
    for i in range(k):
        a = pakka.popleft()
        b = pakka.popleft()
        pakka.append(b)
        pakka.append(a)
    return pakka[0]

if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11