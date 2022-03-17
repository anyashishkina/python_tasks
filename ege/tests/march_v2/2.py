print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = (a <= b) and not(b == c) and (d <= a)
                if f == True:
                    print(a, b, c, d)
