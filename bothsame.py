def count(s):
    characters = {}
    counter = 0
    for i in range(len(s)):
        if s[i] in characters:
            characters[s[i]] += 1
        else:
            characters[s[i]] = 1
        counter += characters[s[i]]
    return counter

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abcd")) # 4
    print(count("ababca")) # 10