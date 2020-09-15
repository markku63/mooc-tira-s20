def calculate(s):
    # generoidaan kaksi saman pitusta kuin s merkkijonoa joissa on vuorotellen ykkösiä ja
    # nollia, toinen alkaen nollasta ja toinen ykkösestä. Lasketaan erot s:n kanssa ja
    # palautetaan minimi

    n = len(s)
    s1 = "01" * (n // 2)
    s2 = "10" * (n // 2)
    if n % 2 != 0:
        s1 += "0"
        s2 += "1"
    x1 = int(s, 2) ^ int(s1, 2)
    x2 = int(s, 2) ^ int(s2, 2)
    return min(bin(x1).count("1"), bin(x2).count("1"))


if __name__ == "__main__":
    print(calculate("1010")) # 0
    print(calculate("1111")) # 2
    print(calculate("10010001")) # 3