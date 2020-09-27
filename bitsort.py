def solve(s):
    zeros = 0
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            zeros += 1
        else:
            count += zeros
    return count
    


if __name__ == "__main__":
    print(solve("000100")) # 2
    print(solve("111000")) # 9
    print(solve("101010")) # 6