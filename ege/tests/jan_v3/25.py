for n in range(245690, 245757):
    cnt = 0 
    for d in range(2, n):
        if n % d == 0:
            cnt += 1 
    if cnt == 0:
        print(n)
