for x in range(10000, 100000):
    for y in range(10000, 100000):
        a = 0
        b = 0
        while x * y > 0:
            if x > 0:
                a = a + 1
            if (y > 0) and (y % 7 > b):
                b = y % 7
            x = x // 10
            y = y // 7
        if (a == 4) and (b == 5):
            print(x, y)
            break
