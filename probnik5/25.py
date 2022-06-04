for n in range(450001, 1000000):
    div = set()
    for d in range(2, n):
        if n % d == 0:
            div2 = set()
            for d2 in range(2, d):
                if d % d2 == 0:
                    div2.add(d2)
                    div2.add(d//d2)
            if len(div2) == 0:
                div.add(d)
                div.add(n//d)
    if len(div) != 0:
        if (max(div) - min(div)) % 29 == 11:
            print(n, max(div) - min(div))
