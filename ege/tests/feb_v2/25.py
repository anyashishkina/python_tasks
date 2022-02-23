cnt = 0 
for n in range(452021+1,100000000):
    min_d, m = 10000000, 0
    for d in range(2, n):
        if n % d == 0:
            min_d = d 
    m = n / min_d + min_d 
    if m % 7 == 3:
        print(n, m)
        cnt += 1 
        if cnt >= 5:
            break
