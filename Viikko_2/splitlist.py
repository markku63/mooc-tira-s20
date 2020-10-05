def count(t):
    if len(t) < 2:
        # alle kahden alkion  listaa ei voi jakaa
        return 0

    # vasemman puolen suurin < oikean puolen pienin
    vmax = []
    vmax.append(t[0])
    for i in range(1, len(t) - 1):
        vmax.append(max(vmax[i - 1], t[i]))

    omin = [0] * (len(t) - 1)
    omin [-1] = t[-1]
    for i in range(len(t) - 3, -1, -1):
        omin[i] = min(omin[i + 1], t[i + 1])

    laskuri = 0
    for i in range(len(t)-1):
        if vmax[i] < omin[i]:
            laskuri += 1
    return laskuri

if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 4
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3