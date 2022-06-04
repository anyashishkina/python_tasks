f = open('26-50.txt')
n = int(f.readline())
d = [int(x) for x in f]
cnt, cnt1, cnt2 = 0, 0, 0
a = []
for i in range(n):
    for j in range(i+1, n):
        if (d[i] + d[j]) % 2 == 0:
            for k in range(n):
                if d[k] < ((d[i] + d[j])/2):
                    cnt1 += 1
                if d[k] > ((d[i] + d[j])/2):
                    cnt2 += 1
            if (cnt1 >= 2500) and (cnt2 >= 1250):
                cnt += 1
                a.append((d[i] + d[j])/2)
print(cnt, min(a))
