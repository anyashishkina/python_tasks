from functools import * 
@lru_cache
def F(n):
    if n == 0:
        return 8 
    elif (n > 0) and (n%3==0):
        return 5 + F(n // 3)
    else:
        return F(n // 3)

cnt = 0 
for n in range(1, 100000000):
    if F(n) == 18:
        cnt += 1 

print(cnt)
