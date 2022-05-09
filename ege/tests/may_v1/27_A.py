f = open('27-A (3).txt')
n = int(f.readline())
d = [int(x) for x in f]
max_s = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(i+2, n):
            if (d[i] + d[j] + d[k]) % 3 == 0:
                max_s = max(max_s, d[i] + d[j] + d[k])
print(max_s)
