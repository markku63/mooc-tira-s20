from heapq import heappush, heappop

class Tasks:
    def __init__(self) -> None:
        self.jono = []

    def add(self, name: str, priority: int) -> None:
        heappush(self.jono, (-priority, name))

    def next(self) -> str:
        return heappop(self.jono)[1]

if __name__ == "__main__":
    t = Tasks()
    t.add("siivous",10)
    t.add("ulkoilu",50)
    t.add("opiskelu",50)
    print(t.next()) # opiskelu
    t.add("treffit",100)
    print(t.next()) # treffit
    print(t.next()) # ulkoilu