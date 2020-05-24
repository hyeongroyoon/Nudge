from FD_Superkey import *

#제3 정규형 검사 코드
def is_3nf(S, F):
    if is_bcnf(S, F):
        return True
    PA = set([])
    T = [set(x) for x in candkey(S, F)]
    for i in T:
        PA = PA | i
    for X, Y in F:
        if Y.issubset(PA):
            return True
        else:
            return False
    return True


#BCNF 검사 코드
def is_bcnf(S,F):
    for X, Y in F:
        if not is_superkey(X, S, F):
            return False
    return True
