def count(s):
    counter = 0
    run = 0
    prev = ""
    for i in range(len(s)):
        if s[i] == prev:
            run += 1   
        else:
            run = 1
            prev = s[i]
        counter += run 
    return counter
    
if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5