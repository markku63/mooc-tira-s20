from random import randint

def count(t):
    last = {}
    count = 0
    result = 0
    for i in range(len(t)):
        if t[i] not in last:
            count += 1
        else:
            count = min(count + 1, i - last[t[i]])
        last[t[i]] = i
        result += count
    return result

if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 15
    print(count([1,1,1,1,1])) # 5
    print(count([1,2,1,1,2])) # 8
