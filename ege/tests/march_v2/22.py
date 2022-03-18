cnt = 0
for x in range(1, 1000000):
    t = str(x)
    x2 = list(t)
    x = (x - x % 8) * 10
    a = 1
    b = 0
    while x > 0:
        if x % 2 != 0:
            a = a * (x % 4)
        else:
            b = b + (x % 4)
        x = x // 8
    for i in range(len(x2)-1):
        if x2[i] > x2[i+1]:
            if a == 9 and b == 5:
                cnt += 1
print(cnt)
