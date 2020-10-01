def count(t,k):
    res = []
    w_beg = 0
    w_end = k - 1
    numbers = {}

    for i in range(k):
        numbers[t[i]] = numbers.get(t[i], 0) + 1
    
    res.append(len(numbers))
    while w_end < len(t)-1:       
        w_end += 1
        numbers[t[w_end]] = numbers.get(t[w_end], 0) + 1
        numbers[t[w_beg]] -= 1
        if numbers[t[w_beg]] == 0:
            del numbers[t[w_beg]]
        w_beg += 1
        res.append(len(numbers))
    return res

if __name__ == "__main__":
    print(count([1,1,2,2],2)) # [1,2,1]
    print(count([1,1,1,1],4)) # [1]
    print(count([1,2,3,2,2,2],3)) # [3,2,2,1]