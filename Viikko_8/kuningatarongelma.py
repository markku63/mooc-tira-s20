from typing import List

n: int = 11
laskuri: int = 0
kohta: List[int] = [-1]*n

def voi_sijoittaa(y: int, x: int ) -> bool:
    global kohta
    for i in range(y):
        if kohta[i] == x:
            return False
        elif abs(i-y) == abs(kohta[i]-x):
            return False
    return True

def haku(y: int) -> None:
    global n, laskuri, kohta
    if y == n:
        laskuri += 1
    else:
        for x in range(n):
            if voi_sijoittaa(y, x):
                kohta[y] = x
                haku(y+1)

haku(0)
print(n, ":", laskuri)