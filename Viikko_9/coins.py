def count(t):
    s = sum(t)
    summat = [False]*(s+1)
    summat[0] = True
    for i in range(len(t)):
        for j in range(s, -1, -1):
            if summat[j]:
                summat[j + t[i]] = True
    return summat.count(True) - 1 # jätetään pois summa == 0



if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91