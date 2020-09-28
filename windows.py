def count(t,k):
    res = []
    for i in range(0, len(t) - k + 1):
        res.append(len(frozenset(t[i:i+k])))
    return res

if __name__ == "__main__":
    print(count([1,1,2,2],2)) # [1,2,1]
    print(count([1,1,1,1],4)) # [1]
    print(count([1,2,3,2,2,2],3)) # [3,2,2,1]