def part(rem, lim):
    if rem < lim:
        return 0
    elif rem == lim:
        return 1
    else:
        return part(rem - lim, lim) + part(rem, lim + 1)

def count(n):
    return part(n, 1)

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174