def count(t):
    lista = sorted(t)
    laskuri = 1
    for i in range(1, len(lista)):
        if lista[i] != lista[i-1]+1:
            laskuri += 1
    return laskuri

if __name__ == "__main__":
    print(count([4,1,5,3])) # 2
    print(count([4,2,1,3])) # 1
    print(count([5,2,7,6,3,9])) # 3