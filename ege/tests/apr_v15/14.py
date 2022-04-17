for x in range(10, 100):
    t = x
    if hex(x)[2:][-1] == 'a':
        s = ''
        while x > 0:
            s = str(x%5) + s
            x //= 5
        if s[-1] == '3':
            print(t)
