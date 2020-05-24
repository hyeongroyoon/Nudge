
# F하의 X의 폐포 찾기
def xplus(X, F):
    Xp = X
    for Y, Z in F:
        if (Y.issubset(Xp)):
            Xp = Xp | Z
    return Xp

# 집합 S에 속한 K가 F하에서 superkey인지 체크
def is_superkey(K, S, F):
    newXp = K
    oldXp = K
    while(1):
        oldXp = newXp
        for Y, Z in F:
            if Y.issubset(newXp):
                newXp = newXp | Z
        if newXp == oldXp:
            break
    return (newXp == S)