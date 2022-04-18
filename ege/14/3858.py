for x in range(1, 10000):
    y = 81**20 - 9**x + 50
    s = ''
    sm = 0
    while y > 0:
        s = str(y%9) + s
        y //= 9
    for i in range(len(s)):
        sm += int(s[i])
    if sm == 138:
        print(x)
        break
    
