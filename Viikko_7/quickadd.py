from heapq import heappush, heappop

class QuickAdd:
    def __init__(self) -> None:
        self.jono = []

    def add(self, k: int, x: int) -> None:
        heappush(self.jono, (x, k))

    def remove(self, k: int) -> int:
        sum = 0
        while k > 0:
            x = heappop(self.jono)
            if x[1] > k:
                heappush(self.jono, (x[0], x[1]-k))
                sum += x[0] * k
                break
            else:
                sum += x[0] * x[1]
                k -= x[1]
        return sum

if __name__ == "__main__":
    q = QuickAdd()
    q.add(5,3)
    print(q.remove(2)) # 6
    q.add(8,1)
    print(q.remove(4)) # 4
    print(q.remove(7)) # 13
    q.add(10**9,123)
    print(q.remove(10**9)) # 123000000000
