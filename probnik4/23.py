from functools import *
@lru_cache
def F(ns, nf):
    if ns == nf:
        return 1
    if ns < nf:
        return 0
    return F(int(bin(ns)[2:]) - 1, nf) + F(int(bin(ns)[2:][:-1], base = 2), nf)
print(F(55, 6))
