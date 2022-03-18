for i in range(10000, 100000):
    x1 = str(i)
    x2 = list(x1)
    s1 = x2[0] + x2[2] + x2[4]
    s2 = x2[1] + x2[3]
    s = str(s1) + str(s2)
    if int(s) == 723:
        print(i)
        break
