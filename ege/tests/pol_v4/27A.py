f = open('27-74a.txt')
n = int(f.readline())
a = [int(x) for x in f]
k1 = 0
for i in range(n):
    s = 0
    k2 = 0
    for j in range(i, n):
        s += a[j]
        k2 += 1
        if s % 39 == 0 and k2 <= 20:
            k1 += 1
print(k1)
