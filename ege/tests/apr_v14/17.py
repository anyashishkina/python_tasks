f = open('17 (11).txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
cnt, max_sum =0, 0
for i in range(len(d)-1):
    for j in range(i+1, len(d)):
        if ((d[i] + d[j])% 2 != 0) and ((d[i] * d[j]) % 3 == 0):
            cnt += 1
            max_sum = max(max_sum, d[i] + d[j])
print(cnt, max_sum)
