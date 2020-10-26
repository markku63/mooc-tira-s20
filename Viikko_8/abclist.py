def create(n):
    if n == 1:
        return ['A', 'B', 'C']
    else:
        res = []
        for s in create(n-1):
            res.append(s + 'A')
            res.append(s + 'B')
            res.append(s + 'C')
        return res

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 243