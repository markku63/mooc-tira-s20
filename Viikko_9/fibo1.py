from time import perf_counter

def fibo(n):
    f = []
    f.append(0)
    f.append(1)
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

n = 40
alku = perf_counter()
tulos = fibo(n)
loppu = perf_counter()
print("Kun n=", n, "funktio palauttaa arvon", tulos, "ja aikaa kuluu", loppu-alku, "sekuntia")

    