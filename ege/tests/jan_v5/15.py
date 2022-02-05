for a in range(1, 1000):
    f = 1 
    for x in range(1, 100):
        for y in range(1, 100):
            if not((x* y < a) or (y > x) or (x >= 8)):
                f = 0 
                break
        if f == 0:
            break
    if f:
        print(a)
        break
