for a in range(1, 300):
    f = 1 
    for x in range(1, 300):
        for y in range(1, 300):
            if not((x > a) or (y > x) or (2*y + x < 110)):
                f = 0 
                break
        if f == 0:
            break
    if f:
        print(a)
