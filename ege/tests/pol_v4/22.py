cnt = 0
for x in range(100000, 10000000):
    L, M = 0, 0
    while x > 0:
        L = L + 1
        if x % 16 % 2 == 0:
            M = M + 1
        else:
            M = M - 1
        x = x // 16
    if L == 6 and M == 0:
        cnt += 1
print(cnt)
