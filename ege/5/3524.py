b =''
for r in range(1, 344):
    while r > 0:
        b = str(r % 6) + b 
        r //= 6 
    r = str(r) + str(r)[-1]
    r = int(r)
    r = bin(r)[2:]
    r = str(r) + str(r)[-1]
    r = int(r, base = 2)
    if r < 344:
        print(r)
        
