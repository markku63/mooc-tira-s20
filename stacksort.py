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
    for i in range(1, len(result)):
        if result[i-1] > result[i]:
            return False
    return True


    
if __name__ == "__main__":
    print(check([4,5,2,3,1])) # True
    print(check([2,3,4,5,1])) # False
    print(check([1,5,2,4,3])) # True
    print(check([4, 2, 5, 1, 3])) # True
    print(check([8, 10, 2, 7, 3, 1, 4, 5, 9, 6]))