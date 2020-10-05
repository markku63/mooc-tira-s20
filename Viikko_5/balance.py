# osajono voi olla balanssissa vain jos sen pituus
# on kolmella jaollinen
# jonon merkkiin i päättyy i//3 osajonoa

def count(s):
    n = len(s)
    count = 0

    if n < 3:
        return 0

    return count

if __name__ == "__main__":
    print(count("CCAABB")) # 1
    print(count("CBACBA")) # 5
    print(count("AAABBC")) # 0