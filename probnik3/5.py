for n in range(1, 1000):
    s = bin(n)[2:]
    if int(s) % 2 == 0:
        s = s +'1'
    else:
        s = s + '0'
    if int(s) % 2 == 0:
        s = s +'1'
    else:
        s = s + '0'
    if int(s, base = 2) < 171:
        print(n)
