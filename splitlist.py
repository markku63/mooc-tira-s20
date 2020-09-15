def count(t):
    # vasemman puolen suurin < oikean puolen pienin
    vmax = -1
    omin = min(t[1:])
    laskuri = 0
    for i in range(len(t)-1):
        vmax = max(vmax, t[i])
        omin = min(t[i+1:])
        if vmax >= omin:
            break
        laskuri += 1

    return laskuri

if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 4
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3