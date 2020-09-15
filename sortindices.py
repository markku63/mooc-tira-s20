def get(t):
    result = [i for i in range(len(t))]
    result.sort(key=lambda i: t[i])
    return result

if __name__ == "__main__":
    print(get([1,2,4,3])) # [0,1,3,2]
    print(get([4,2,1,3])) # [2,1,3,0]
    print(get([6,2,8,5,3])) # [1,4,3,0,2]