from time import perf_counter

kutsuja = 0

def fibo(n):
    global kutsuja
    kutsuja += 1
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

alku = perf_counter()
tulos = fibo(40)
loppu = perf_counter()
print("Tulos=",tulos)
print("Kutsuja",kutsuja)
print("Aika",(loppu-alku))