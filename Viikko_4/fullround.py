def count(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n
    else:
        # return count(n-1) + count(n-2)
        # Tuosta tulee n:ää pienempien parillisten lukujen summa
        # eli:
        i = n // 2
        return i * (i + 1)


if __name__ == "__main__":
    print(count(2)) # 2
    print(count(5)) # 6
    print(count(31)) # 240
    