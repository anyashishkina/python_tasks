from math import sqrt 
cnt = 0
for n in range(800000, 1000000):
    m = 0 
    for d in range(2, int(sqrt(n))+1):
        if n % d == 0:
            min_d = d 
            break 
    m = min_d + n // min_d 
    if m % 138 == 0:
        print(n, m)
        cnt += 1 
        if cnt >= 5:
            break
