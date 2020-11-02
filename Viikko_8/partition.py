def create(word, length, result):
    if len(word) == length:
        result.append(word)
        return
    else:
        create(word+"0", length, result)
        create(word+"1", length, result)

def check(t):
    res = []
    create("", len(t), res)
    for s in res:
        sum1 = 0
        sum2 = 0
        for i, b in enumerate(s):
            if b == "0":
                sum1 += t[i]
            else:
                sum2 += t[i]
        if sum1 == sum2:
            return True
    return False

if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True