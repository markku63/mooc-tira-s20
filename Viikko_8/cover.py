def count_h(n, m, k):
    if k == 1:
        return 1
    elif k == 2:
        return n + m - 2
    else:
        pass

if __name__ == "__main__":
    print(count_h(2,2,4)) # 8
    #print(count(2,3,3)) # 13
    #print(count(4,4,1)) # 1
    #print(count(4,3,10)) # 3146
    #print(count(4,4,16)) # 70878