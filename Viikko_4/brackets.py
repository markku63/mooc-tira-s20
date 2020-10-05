def count(s):
    l = []
    for c in s:
        if len(l) > 0 and c == ')' and l[-1] == '(':
            l.pop()
        else:
            l.append(c)
    return len(l)
    
if __name__ == "__main__":
    print(count("(()())")) # 0
    print(count("))))))")) # 6
    print(count("((())(")) # 2