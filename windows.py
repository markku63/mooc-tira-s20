def count(t,k):
    res = []
    numbers = {}

    for w_end in range(len(t)):       
        numbers[t[w_end]] = numbers.get(t[w_end], 0) + 1
        w_beg = w_end - k + 1
        if w_beg > 0:
            numbers[t[w_beg - 1]] -= 1
            if numbers[t[w_beg - 1]] == 0:
                del numbers[t[w_beg - 1]]
        if w_beg >= 0:
            res.append(len(numbers))

    return res

if __name__ == "__main__":
    print(count([1,1,2,2],2)) # [1,2,1]
    print(count([1,1,1,1],4)) # [1]
    print(count([1,2,3,2,2,2],3)) # [3,2,2,1]