for x in range(1, 10000):
    t = x 
    a=0; b=0
    while x > 0:
        if x%2 == 0:
            a += 1
        else:
            b += x%6
        x = x//6
    if a == 2 and b == 4:
        print(t)
        break
