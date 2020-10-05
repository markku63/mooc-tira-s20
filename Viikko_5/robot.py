
def move(cur, c):
    if c == "L":
        return (cur[0] - 1, cur[1])
    elif c == "R":
        return (cur[0] + 1, cur[1])
    elif c == "U":
        return (cur[0], cur[1] + 1)
    elif c == "D":
        return (cur[0], cur[1] - 1)
    else:
        raise ValueError("No such direction: " + str(c))

def count(s):
    cur = (0, 0)
    locations = {cur: 1}
    for c in s:
        cur = move(cur, c)
        if cur not in locations:
            locations[cur] = 1
        else:
            locations[cur] += 1
    return len(locations)

print(count("LL")) # 3
print(count("UUDLRR")) # 5
print(count("UDUDUDU")) # 2