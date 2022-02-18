cnt = 0
for n in range(2, 1000):
    r = n 
    if r % 2 == 0:
        r //= 2
    else:
        r -= 1 
    if r % 3 == 0:
        r //= 3
    else:
        r -= 1 
    if r % 7 == 0:
        r //= 7 
    else:
        r -= 1 
    if r == 2:
        cnt += 1 
print(cnt)
