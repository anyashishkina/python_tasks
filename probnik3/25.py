for n in range(800000, 1000000):
    div = set()
    for d in range(2, n):
        if n % d == 0:
            div.add(d)
            div.add(n//d)
    if len(div) >= 2:
        if (min(div) + max(div)) % 138 == 0:
            print(n, min(div) + max(div))
