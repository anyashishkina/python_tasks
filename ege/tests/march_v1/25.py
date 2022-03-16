from math import sqrt
for n in range(123456789, 223456789+1):
    div = []
    for d in range(2, int(sqrt(n))+1):
        if n % d == 0:
            div.append(d)
            mirror_d = n // d
            if mirror_d != d:
                div.append(mirror_d)
    if len(div) == 3:
        print(n, div)
