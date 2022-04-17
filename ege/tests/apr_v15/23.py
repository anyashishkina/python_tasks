from functools import *
@lru_cache
def F(ns, nf):
    if ns == nf:
        return 1
    if ns > nf:
        return 0
    return F(ns * 2, nf) + F(ns * 2 + 1, nf)
cnt = 0
for nf in range(2, 100000):
    if F(1, nf) == 10:
        cnt += 1

print(cnt)
