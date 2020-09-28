def polyhajautus(s, n):
    A = 7
    arvo = 0
    for k, c in enumerate(reversed(s)):
        arvo += A ** k * ord(c)
    return arvo % n

n = 10 ** 5
print(polyhajautus("testi", n))
print(polyhajautus("apina", n))
print(polyhajautus("banaani",  n))
print(polyhajautus("cembalo", n))