from time import perf_counter

n = 40
f = [0]*(n+1)
f[0] = 0
f[1] = 1

def fibo(n):
    if n <= 1:
        return n
    elif f[n] != 0:
        return f[n]
    else:
        f[n] = fibo(n -1) + fibo(n - 2)
        return f[n]

alku = perf_counter()
tulos = fibo(n)
loppu = perf_counter()
print("Kun n=", n, "funktio palauttaa arvon", tulos, "ja aikaa kuluu", loppu-alku, "sekuntia")
