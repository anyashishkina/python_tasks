from math import sqrt

for n in range(45000000, 50000000):
    div = []
    for d in range(2, int(sqrt(n))+1):
        if n % d == 0:
            div.append(d)
            mirror_d = n // d
            if mirror_d != d:
                div.append(mirror_d)
if len(div) == 5:
    print(n)
