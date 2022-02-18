for n in range(2, 100):
    r = n 
    r = bin(r)[2:]
    r = str(r) + str(r[-2])
    r = str(r) + str(r[1])
    r = int(r, base = 2)
    if r >= 190:
        print(n)
        break
