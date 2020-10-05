def count(s):
    osajonot = set()
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            osajonot.add(s[i:j+1])
    return len(osajonot)
 
if __name__ == "__main__":
    print(count("aaa")) # 3
    print(count("abc")) # 6
    print(count("saippuakauppias")) # 110