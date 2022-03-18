from functools import *
@lru_cache
def F(n):
    if n <= 3:
        return n + 3
    if n > 3 and F(n-1)%2 == 0:
        return F(n-2) + n
    if n > 3 and F(n-1)% 2 != 0:
        return F(n-2) + 2*n
k = 0
for i in range(40, 51):
    k = k + F(i)
print(k)
        
