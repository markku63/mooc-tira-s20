def create(s: str) -> list[str]:
    if len(s) <= 1:
        return [s]

if __name__ == "__main__":
    #print(create("ab")) # [ab,ba]
    #print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    #print(len(create("aybabtu"))) # 1260
    print(create("a"))