def count(n,a,b):
    jumps = [0] * (n + 1)
    jumps[a] = 1
    for i in range(2*a, b, a):
        jumps[i] = 1
    jumps[b] = 2 if b % a == 0 else 1

    for i in range(b + 1, n + 1):
        jumps[i] = jumps[i-a] + jumps[i-b]
    return jumps[n]

if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456