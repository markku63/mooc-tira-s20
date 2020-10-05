# https://en.wikipedia.org/wiki/Partition_(number_theory)#Odd_parts_and_distinct_parts
# https://math.stackexchange.com/a/1938523

def count(n):
    if n < 6:
        return 0
    k = n // 6
    if n % 6 == 0:
        return 3 * k * k - 3 * k + 1
    if n % 6 == 1:
        return 3 * k * k - 2 * k
    if n % 6 == 2:
        return 3 * k * k - k
    if n % 6 == 3:
        return 3 * k * k
    if n % 6 == 4:
        return 3 * k * k + k
    if n % 6 == 5:
        return 3 * k * k + 2 * k

if __name__ == "__main__":
    print(count(8)) # 2
    print(count(30)) # 61
    print(count(1337)) # 148296