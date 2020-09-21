from time import perf_counter

class Node(object):
    def __init__(self, data = None):
        super().__init__()
        self.__next = None
        self.__data = data

class LinkedList(object):
    def __init__(self):
        super().__init__()
        self.__start = None
        self.__end = None

    def append(self, data):
        new_node = Node(data)
        if self.__start == None:
            self.__start = new_node
            self.__end = new_node
        else:
            self.__end._Node__next = new_node
            self.__end = new_node

    def popleft(self):
        if self.__start == None:
            raise IndexError('Tyhjä lista')
        else:
            self.__start = self.__start._Node__next
            if self.__start == None:
                self.__end = None

n = 10**5
lista = LinkedList()
alku = perf_counter()
for i in range(1, n+1):
    lista.append(i)
loppu = perf_counter()
print("Lisäämiseen kului: ", loppu - alku, " sekuntia")

alku = perf_counter()
for i in range(n):
    lista.popleft()
loppu = perf_counter()
print("Poistamiseen kului: ", loppu - alku, " sekuntia")
