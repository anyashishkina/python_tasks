f = open('17-278 (1).txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break 
    d.append(int(s))
sm, cnt, max_sum = 0, 0, 0
for i in range(len(d)):
    if d[i] % 12 == 0:
        s = ''
        while d[i] > 0:
            s = str(d[i] % 5) + s 
            d[i] // 5
        sm += s.count('4') * 4
for i in range(len(d)-1):
    if (d[i] > sm) and (d[i+1] > sm):
        cnt += 1 
        max_sum = max(max_sum, d[i] + d[i+1])
print(cnt, max_sum)
