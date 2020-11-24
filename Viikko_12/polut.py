def polut(x):
    pit = [0]*(x+1)
    pit[1] = 1
    pit[2] = 1
    for i in range(3, x+1):
        pit[i] = pit[i-1] + pit[i-2]
    return pit[x]

print(polut(50))