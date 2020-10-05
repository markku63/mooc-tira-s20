def create(n):
    lista = []
    for i in range(n):
        if i % 2 != 0:
            lista.append(i+1)
        else:
            lista.insert(0, i+1)
    return lista
 
if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]