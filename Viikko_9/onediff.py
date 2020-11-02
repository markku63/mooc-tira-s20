def find(t):
    pisin = [1]*len(t)
    for k in range(len(t)):
        for x in range(k):
            if abs(t[x] - t[k]) == 1 and pisin[x] + 1 > pisin[k]:
                pisin[k] = pisin[x]+1
    return max(pisin)

if __name__ == "__main__":
    print(find([1,2,3,4,5])) # 5
    print(find([5,5,5,5,5])) # 1
    print(find([5,2,3,8,2,4,1])) # 4