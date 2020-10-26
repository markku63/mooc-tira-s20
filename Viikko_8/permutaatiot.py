n = 9
luvut = [None]*n
mukana = [False]*n
jarjestys = 0

def haku(k):
    global n, jarjestys, luvut, mukana
    if k == n:
        jarjestys += 1
        if jarjestys == 54321:
            print(jarjestys, luvut)
    else:
        for i in range(n):
            if not mukana[i]:
                mukana[i] = True
                luvut[k] = i + 1
                haku(k+1)
                mukana[i] = False

haku(0)