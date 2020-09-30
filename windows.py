def count(t,k):
    res = []
    w_beg = 0
    w_end = k
    num_set = set(t[0:k])

    while w_end <= len(t):
        res.append(len(num_set))
        
    return res

if __name__ == "__main__":
    print(count([1,1,2,2],2)) # [1,2,1]
    print(count([1,1,1,1],4)) # [1]
    print(count([1,2,3,2,2,2],3)) # [3,2,2,1]