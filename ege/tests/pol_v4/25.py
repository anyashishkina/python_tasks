from math import sqrt
for n in range(912673, 1, -2):
    div = []
    for d in range(2, int(sqrt(n))+1):
        cnt = 0
        if n % d == 0:
            for d2 in range(2, int(sqrt(d))+1):
                if (d % d2 == 0) and (int(sqrt(d)) == d//d2):
                    cnt += 1
                if (d % d2 == 0) and (int(sqrt(d)) != d//d2):
                    cnt += 2
            if cnt == 0:
                div.append(d)
    if sum(div) != 0:
        if n % sum(div) == 0:
            print(n, sum(div))
