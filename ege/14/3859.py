for x in range(1, 100000):
    y = 64**12 - 8**14 + x
    s = oct(y)[2:]
    if s.count('7') == 12 and s.count('1') == 1:
        print(x)
        break
    
