def count(t):
    count = 0
    charsets = {}
    for w in t:
        chars = frozenset(w)
        n = charsets.setdefault(chars, 0)
        count += n
        charsets[chars] = n + 1
    
    return count


if __name__ == "__main__":
    print(count(["A","AA","AAA"])) # 3
    print(count(["A","B","C"])) # 0
    print(count(["KALA","ALA","LAKKA"])) # 1