f = open('27-76a.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
cnt = 0
for i in range(0, n - 2):
    for j in range(i + 2, n):
        if ((a[i] + a[j]) % 3 == 0) and (sum(a[i+1:j])% 2 == 0):
            cnt += 1
print(cnt)
