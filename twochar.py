# Esimerkkiratkaisu
def count(s):
    pos1 = pos2 = -1
    result = 0
    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            if pos1 == -1 or s[i] != s[pos1]:
                pos2 = pos1
            pos1 = i-1
        result += pos1-pos2
    return result

if __name__ == "__main__":
    print(count("aaaa")) # 0
    print(count("abab")) # 6
    print(count("aabacba")) # 8