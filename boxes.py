from collections import deque

def count(t,x):
    items = deque(sorted(t))
    full_bins = 0
    while len(items) > 0:
        item = items.pop()
        full_bins += 1
        if len(items) > 0 and items[0] + item <= x:
            items.popleft()
    return full_bins

if __name__ == "__main__":
    print(count([1,2,3,4],10)) # 2
    print(count([4,4,4,4],5)) # 4
    print(count([7,2,3,9],10)) # 3
