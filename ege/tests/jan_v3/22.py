for x in range(1, 1000):
    t = x
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if M < x and x % 2 == 0:
            M = x % 10
        x = x // 10
    if L == 3 and M == 8:
        print(t)
        break
