from collections import deque

def count2(n):
    def rotate(q):
        tmp = q.popleft()
        q.rotate(-1)
        q.append(tmp)

    def check(q):
        for i in range(1, len(q)):
            if q[i-1] > q[i]:
                return False
        return True


    q = deque(range(1, n+1))
    rotate(q)
    steps = 1
    while not check(q):
        rotate(q)
        steps += 1
    return steps

def count(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n
    else:
        return n-1 + count(n-2)


if __name__ == "__main__":
    for i in range(2, 10**3):
        if count(i) != count2(i):
            print("Fail!", i)
    #print(count(2)) # 2
    #print(count(5)) # 6
    #print(count(31)) # 240