for x in range(1, 100000):
    y = 27**7 - 3**11 + 36 - x
    s = ''
    sm = 0 
    while y > 0:
        s = str(y%3) + s
        y //= 3
    for i in range(len(s)):
        sm += int(s[i])
    if sm == 22:
        print(x)
        break
    
