def create(n):
    if n == 1:
        return ['A', 'B', 'C']
    else:
        res = []
        for s in create(n-1):
            for c in range(ord('A'), ord('D')):
                if ord(s[-1]) != c:
                    res.append(s + chr(c))
        return res

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AB,AC,BA,BC,CA,CB]
    print(len(create(5))) # 48