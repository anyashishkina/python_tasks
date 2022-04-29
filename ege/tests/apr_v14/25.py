from math import *
for n in range(11000000, 12000000):
    div = set()
    m = 0
    for d in range(2, int(sqrt(n))-1):
        if n % d == 0:
            div.add(n//d)
        if len(div) == 2:
            break
    if len(div) == 1:
        m = 0
    if len(div) == 2:
        m = sum(div)
        if (m > 0) and (m < 10000):
            print(n, m)
