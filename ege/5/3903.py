for n in range(2, 70):
    r = n 
    r = bin(r)[2:]
    if r.count('1') == r.count('0'):
        r = str(r) + str(r[-1])
    else:
        if r.count('1') > r.count('0'):
            r = str(r) + '0' 
        else:
            r = str(r) + '1'
    if r.count('1') == r.count('0'):
        r = str(r) + str(r[-1])
    else:
        if r.count('1') > r.count('0'):
            r = str(r) + '0' 
        else:
            r = str(r) + '1'
    if r.count('1') == r.count('0'):
        r = str(r) + str(r[-1])
    else:
        if r.count('1') > r.count('0'):
            r = str(r) + '0' 
        else:
            r = str(r) + '1'
    if r.count('1') == r.count('0'):
        r = str(r) + str(r[-1])
    else:
        if r.count('1') > r.count('0'):
            r = str(r) + '0' 
        else:
            r = str(r) + '1'
    r = int(r, base = 2)
    if r % 4 == 0:
        print(n)
