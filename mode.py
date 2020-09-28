from operator import itemgetter

class Mode:
    def __init__(self):
        self.__luvut = {}
        self.__moodi = (0, 0) # (luku, määrä)

    def add(self, x):
        if x not in self.__luvut:
            self.__luvut[x] = 1
        else:
            self.__luvut[x] += 1
        if self.__luvut[x] > self.__moodi[1] or (self.__luvut[x] == self.__moodi[1] and x < self.__moodi[0]):
            self.__moodi = (x, self.__luvut[x])
        return self.__moodi[0]

if __name__ == "__main__":
    m = Mode()
    print(m.add(1)) # 1
    print(m.add(2)) # 1
    print(m.add(2)) # 2
    print(m.add(1)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 3