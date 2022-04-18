from math import sqrt
for n in range(500000000, 550000000):
    m, cnt = 1, 0
    for d in range(2, int(sqrt(n)+1)):
        if n % d == 0:
            cnt += 1
            m *= d
            if n // d != n % d:
                cnt += 1
                m *= (n//d)
    if cnt < 5:
        m = 0
    if (cnt == 5) and (m > 0) and (m < n):
        print(m, n)
