from random import shuffle

def check(t):
    if len(t) < 2:
        # Yhden elementin lista on aina järjestyksessä
        return True

    stk1 = []
    stk2 = []
    result = []
    # https://faculty.math.illinois.edu/~west/regs/stacksort.html
    for i in t:
        while True:
            # sijoitetaan tyhjään pinoon jos sellainen löytyy
            if len(stk1) == 0:
                stk1.append(i)
                break
            elif len(stk2) == 0:
                stk2.append(i)
                break
            # jos molempien pinojen päällimmäinen luku on sijoitettavaa
            # pienempi, popataan pienempi luku tulokseen ja yritetään uudelleen
            elif i >= stk1[-1] and i >= stk2[-1]:
                if stk1[-1] < stk2[-1]:
                    result.append(stk1.pop())
                else:
                    result.append(stk2.pop())
            else:
                # jos molempien pinojen päällimmäinen on suurempi kuin 
                # sijoitettava numero, työnnetään pinoon jonka päällimmäinen on
                # pienempi
                if i < stk1[-1] and i < stk2[-1]:
                    if stk1[-1] < stk2[-1]:
                        stk1.append(i)
                    else:
                        stk2.append(i)
                # muutoin siihen pinoon jonka päällimmäinen on suurempi kuin
                # sijoitettava.
                elif i < stk1[-1]:
                    stk1.append(i)
                else:
                    stk2.append(i)
                break
    
    # tyhjennetään pinot tulokseen
    while len(stk1) > 0 and len(stk2) > 0:
        if stk1[-1] < stk2[-1]:
            result.append(stk1.pop())
        else:
            result.append(stk2.pop())
    while len(stk1) > 0:
        result.append(stk1.pop())
    while len(stk2) > 0:
        result.append(stk2.pop())
    # Tarkistetaan tulos
    for i in range(1, len(result)):
        if result[i-1] > result[i]:
            return False
    return True

def check2(t):
    n = len(t)
    ways = ["0", "1"]
    while len(ways) < 2**n:
        temp = []
        for w in ways:
            temp.append(w+"0")
            temp.append(w+"1")
        ways = temp
    for w in ways:
        stack1 = []
        stack2 = []
        next = 1
        for i in range(n):
            if w[i] == "0":
                stack1.append(t[i])
            else:
                stack2.append(t[i])
            while True:
                if len(stack1) > 0 and stack1[-1] == next:
                    stack1.pop()
                    next += 1
                elif len(stack2) > 0 and stack2[-1] == next:
                    stack2.pop()
                    next += 1
                else:
                    break
        if next == n + 1:
            return True
    return False

    
if __name__ == "__main__":
    n = 3
    while True:
        input = list(range(1, n+1))
        shuffle(input)
        if check(input) != check2(input):
            print(input)
            break

    #print(check([4,5,2,3,1]) == check2([4,5,2,3,1])) # True
    #print(check([2,3,4,5,1]) == check2([2,3,4,5,1])) # False
    #print(check([1,5,2,4,3]) == check2([1,5,2,4,3])) # True
    #print(check([4, 2, 5, 1, 3]) == check2([4, 2, 5, 1, 3])) # True
    #print(check([8, 10, 2, 7, 3, 1, 4, 5, 9, 6]) == check2([8, 10, 2, 7, 3, 1, 4, 5, 9, 6]))