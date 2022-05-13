f =  open('27-76a.txt')
n = int(f.readline())
d = [int(x) for x in f]
cnt = 0
for i in range(n):
    for j in range(i+2, n):
        if (len(d[i:j]) >= 1):
            if ((d[i] + d[j])%3 == 0) and (sum(d[i:j])%2 == 0):
                cnt += 1
print(cnt)
