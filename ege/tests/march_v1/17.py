f = open('17 (10).txt')
d = []
cnt, max_s = 0, 0
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d)-1):
    for j in range(i+1, len(d)):
        if ((d[i] % 160) != (d[j] % 160)) and ((d[i] % 7 == 0) or (d[j] % 7 == 0)):
            cnt += 1
            max_s = max(max_s, d[i] + d[j])

print(cnt, max_s)

