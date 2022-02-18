for n in range(2, 1000):
    r = n 
    r = bin(r)[2:]
    if r.count('1') > r.count('0'):
        r = str(r) + '1'
    else:
        r = str(r) + '0'
    if r.count('1') > r.count('0'):
        r = str(r) + '1'
    else:
        r = str(r) + '0'
    r = int(r, base = 2)
    if r < 57:
        print(r)
