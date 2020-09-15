def changes(t):
    result = 0
    for i in range(1, len(t)):
        if t[i] < t[i - 1]:
            result += t[i - 1] - t[i]
            t[i] = t[i - 1]
    return result


if __name__ == "__main__":
    print(changes([3,2,5,1,7])) # 5
    print(changes([1,2,3,4,5])) # 0
    print(changes([3,3,1,4,2])) # 4