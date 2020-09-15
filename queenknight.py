def ei_uhkaa(q, k):
    # Kuningatar uhkaa ratsua
    if q[0] == k[0] or q[1] == k[1] or abs(q[0] - k[0]) == abs(q[1] - k[1]):
        return False
    # Ratsu uhkaa kuningatarta
    if abs(q[0] -k[0]) == 2 and abs(q[1] - k[1]) == 1 or \
        abs(q[0] - k[0]) == 1 and abs(q[1] - k[1]) == 2:
        return False
    return True

def count(n):
    c = 0
    if n < 2:
        # 1 ruudun laudalle ei mahdu kahta nappulaa
        return 0
    for qx in range(n):
        for qy in range(n):
            for kx in range(n):
                for ky in range(n):
                    if  (qx != kx and qy != ky) and ei_uhkaa((qx, qy), (kx, ky)):
                        c +=1 
    return c

if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184
