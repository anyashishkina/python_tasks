print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = a and not(b) or (a or b) and c or d
                if f == False:
                    print(a, b, c, d)
