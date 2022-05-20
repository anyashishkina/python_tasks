for a in range(1000):
    f = 1
    for x in range(1000):
        for y in range(1000):
            if not(((5*x - 6*y) < a) or ((x - y) > 30)):
                f = 0
        if f == 0:
            break
    if f:
        print(a)
        break
