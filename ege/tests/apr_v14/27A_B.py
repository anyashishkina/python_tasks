f = open('27985_B (1).txt')
n = int(f.readline())
d = [int(x) for x in f]
pr_max = 0
for i in range(n-1):
    for j in range(i+2, n):
        if (d[i] * d[j]) % 14 == 0:
            pr_max = max(pr_max, d[i] * d[j])
            
print(pr_max)
