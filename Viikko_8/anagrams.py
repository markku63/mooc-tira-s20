def create2(prefix, ft, res):
    if len(ft) == 0:
        res.append(prefix)
    else:
        for char, count in ft.items():
            nft = dict(ft)
            if count == 1:
                del nft[char]
            else:
                nft[char]=count-1
            create2(prefix+char, nft, res)

def create(s):
    ft = {}
    for char in sorted(s):
        ft[char] = ft.get(char, 0) + 1
    res = []
    create2("", ft, res)
    return res

if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260
    print(create("ccbcc"))