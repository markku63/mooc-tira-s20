def count(n):
    sum = 0
    depth = n.bit_length() - 1
    # täydet tasot
    for i in range (1, depth):
        sum += 2**i * i
    # viimeinen taso
    sum += depth * (n - 2**(depth) + 1)
    return sum

if __name__ == "__main__":
    print(count(4)) # 4
    print(count(7)) # 10
    print(count(123)) # 618
    print(count(999999999)) # 27926258178