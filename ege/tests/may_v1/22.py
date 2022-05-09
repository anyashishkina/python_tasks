for x in range(101, 1000):
    t = x
    L = 2*x-30
    M = 2*x+30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 30:
        print(t)
