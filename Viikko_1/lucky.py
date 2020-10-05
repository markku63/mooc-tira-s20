def check(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s % 7 == 0
 
if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True