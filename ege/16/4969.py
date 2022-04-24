from functools import * 
@lru_cache
def F(n):
    if n == 0:
        return 3
    elif (n > 0) and (n%2==0):
        return 1 + F(n // 2)
    else:
        return F(n // 2)

cnt = 0 
for n in range(1, 1000000000):
    if F(n) == 7:
        cnt += 1 

print(cnt)
