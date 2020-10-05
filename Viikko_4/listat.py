from time import perf_counter
from collections import deque

lista = []
pakka = deque()
n = 10**5

# Testi 1
alku = perf_counter()
for i in range(n):
    lista.append(n+1)
for i in range(n):
    lista.pop()
loppu = perf_counter()
print("Listalla kului aikaa ", (loppu - alku), " sekuntia")

alku = perf_counter()
for i in range(n):
    pakka.append(n+1)
for i in range(n):
    pakka.pop()
loppu = perf_counter()
print("Pakalla kului aikaa ", (loppu - alku), " sekuntia")

lista.clear()
pakka.clear()

# Testi 2
alku = perf_counter()
for i in range(n):
    lista.append(n+1)
for i in range(n):
    lista.pop(0)
loppu = perf_counter()
print("Listalla kului aikaa ", (loppu - alku), " sekuntia")

alku = perf_counter()
for i in range(n):
    pakka.append(n+1)
for i in range(n):
    pakka.popleft()
loppu = perf_counter()
print("Pakalla kului aikaa ", (loppu - alku), " sekuntia")