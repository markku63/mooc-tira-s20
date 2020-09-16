from collections import deque

def count(t,x):
    # TODO
    items = deque(sorted(t))
    full_bins = 0
    current_bin = 0
    for i in range(len(items)):
        if i % 2 == 0:
            item = items.pop()
        else:
            item = items.popleft()
        if current_bin == 0:
            current_bin = item
        elif current_bin + item <= x:
            full_bins += 1
            current_bin = 0
        else:
            full_bins += 1
            current_bin = item
    return full_bins + (1 if current_bin != 0 else 0)

if __name__ == "__main__":
    print(count([1,2,3,4],10)) # 2
    print(count([4,4,4,4],5)) # 4
    print(count([7,2,3,9],10)) # 3
    print(count([1, 2, 3, 4, 5], 6)) # 3
    print(count([1, 3, 5, 999999999, 1000000000, 1000000000], 1000000000)) # 4