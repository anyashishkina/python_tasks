for n in range(1, 1000):
    s = bin(n)[2:]
    x = ''
    x = s + s[-1]
    if s.count('1') % 2 == 0:
        x = x + '0'
    else:
        x = x + '1'
    if x.count('1') % 2 == 0:
        x = x + '0'
    else:
        x = x + '1'
    if int(x, base = 2) > 105:
        print(int(x, base = 2))
        break
