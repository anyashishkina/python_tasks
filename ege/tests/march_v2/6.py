cnt = 0 
for s in range(1, 1000000):
    t = s
    n = 10
    while s - n < 1000:
        s = s + n
        n = n + 5
    if n == 80:
        cnt += 1
print(cnt)
