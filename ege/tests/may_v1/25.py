from functools import *
@lru_cache
def f(n):
    div = set()
    for d in range(2, n):
        if (n % d == 0) and (d % 2 != 0):
            div.add(d)
            div.add(n//d)
    return div

for i in range(35000000, 40000000+1):
    div = f(i)
    if len(div) == 5:
        print(i)
