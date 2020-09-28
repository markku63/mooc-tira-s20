from random import randint

PIT = 20
MAARA = 10 ** 6

arvot = {}
uniikkeja = 0
samoja = 0

def sat_jono():
    return "".join(chr(randint(ord("a"), ord("z"))) for i in range(PIT))

for i in range(MAARA):
    h = hash(sat_jono())
    if h not in arvot:
        arvot[h] = 1
    else:
        arvot[h] += 1

print("Eri hajautusarvoja: ", len(arvot))
for n in arvot.values():
    if n == 1:
        uniikkeja += 1
    samoja = max(samoja, n)

print(uniikkeja, "merkkijonolla on hajautusarvo, jota ei ole millään toisella merkkijonolla")
print("Enintään ",samoja, "samaa hajautusarvoa")
