for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x*y < 100) or ( y >= a) or (x > a)):
                f = 0
        if f == 0:
            break
    if f:
        print(a)
