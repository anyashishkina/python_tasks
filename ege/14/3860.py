for x in range(1, 100000):
    y = 125**7 - 25**4 + x
    s = ''
    sm = 0 
    while y > 0:
        s = str(y%5) + s
        y //= 5
    if s.count('4') == 15 and s.count('3') == 1 and s.count('1') == 2:
        print(x)
        break
    
