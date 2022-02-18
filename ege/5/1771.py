for n in range(1, 256):
    r = n
    r = bin(r)[2:]
    r = str(r) + str(r[-1])
    if r.count('1') % 2 == 0:
        r = str(r) + '0'
    else:
        r = str(r) + '1'
    if r.count('1') % 2 == 0:
        r = str(r) + '0'
    else:
        r = str(r) + '1'
    r = int(r, base = 2)
    if r > 144:
        print(r)
        break
