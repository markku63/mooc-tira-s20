from time import perf_counter

count = 0
n = 100000
alku = perf_counter()
for i in range(2, n+1):
    prime = True
    for j in range(2, i):
        if i%j == 0:
            prime = False
            break
    if prime:
        count += 1
loppu = perf_counter()
print("Alkulukuja:",count)
print("Aika:",loppu - alku)