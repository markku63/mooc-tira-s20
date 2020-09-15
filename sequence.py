def kuvaus(s):
    palautettava = ""
    while len(s) > 0:
        d = s[0]
        uusi_s = s.lstrip(d)
        n = len(s) - len(uusi_s)
        palautettava = palautettava + "{}{}".format(n, d)
        s = uusi_s
    return palautettava

def generate(n):
    if n == 1:
        return "1"
    else:
        return kuvaus(generate(n - 1))

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 11
    print(generate(3)) # 21
    print(generate(4)) # 1211
    print(generate(5)) # 111221
