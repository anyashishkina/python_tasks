for x in range(1, 10000):
    t = x
    a = 1
    b = 0
    while x > 0:
        c = x % 10
        a = a*c
        if c > b:
            b = c
        x //= 10
    if a == 48 and b == 6:
        print(t)
        break
