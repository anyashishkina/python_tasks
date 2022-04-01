f = open('27-75a.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
max_s, max_k = 0, 10000000000
for i in range(n-1):
    k = 1
    sum_s = a[i]
    for j in range(i+1, n):
        sum_s += a[j]
        k += 1
        if sum_s % 43 == 0:
            if sum_s > max_s:
                max_s = sum_s
                max_k = k
print(max_k)
