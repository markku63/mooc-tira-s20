from time import perf_counter

count = 0
n = 100000
a = [0 for i in range(n+1)]
alku = perf_counter()
for i in range(2, n+1):
    if a[i] == 0:
        count += 1
        for j in range(2*i, n+1, i):
            a[j] = 1
loppu = perf_counter()
print("Alkulukuja:",count)
print("Aika:",loppu - alku)