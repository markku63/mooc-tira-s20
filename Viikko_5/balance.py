# osajono voi olla balanssissa vain jos sen pituus
# on kolmella jaollinen
# jonon merkkiin i päättyy i//3 osajonoa

def count(s):
    n = len(s)
    count = 0
    counters = {'A': 0, 'B': 0, 'C': 0}
    if n < 3:
        return 0
    for i in range(n):
        counters[s[i]] += 1
        if counters['A'] == counters['B'] and counters['B'] == counters['C']:
            count += 1
    return count

if __name__ == "__main__":
    print(count("CCAABB")) # 1
    print(count("CBACBA")) # 5
    print(count("AAABBC")) # 0
    print(count("ABACAB")) # 2