for x in range(1, 10000):
    y = 36**17 - 6**x + 71
    s = ''
    sm = 0
    while y > 0:
        s = str(y%6) + s
        y //= 6
    for i in range(len(s)):
        sm += int(s[i])
    if sm == 61:
        print(x)
        break
    
