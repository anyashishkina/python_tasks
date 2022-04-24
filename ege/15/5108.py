for a in range(1000, 10000):
    f = 1 
    for x in range(1, 1000):
        if not(((x % 175 != 0) or (x % 25 != 0)) or (2*x + a >= 1780)):
            f = 0 
    if f:
        print(a)
        break
