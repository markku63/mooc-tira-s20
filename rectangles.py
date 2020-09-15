def alue(sk):
    return (sk[2] - sk[0]) * (sk[1] - sk[3])

# Suorakulmioiden leikkausalgoritmi: https://math.stackexchange.com/a/99576
# Muokattu toimimaan N suorakulmion listalle.
def leikkausalue(kulmiot):
    vasemmat, ylat, oikeat, alat = zip(*kulmiot)
    x_leikkaus = max([0, min(oikeat) - max(vasemmat)])
    y_leikkaus = max([0, min(ylat) - max(alat)])
    return x_leikkaus * y_leikkaus

def area(rec1, rec2, rec3):
    # Sovelletaan seulaperiaatetta: https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
    return alue(rec1) + alue(rec2) + alue(rec3) - leikkausalue([rec1, rec2]) \
            - leikkausalue([rec1, rec3]) - leikkausalue([rec2, rec3]) \
            + leikkausalue([rec1, rec2, rec3])

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16
