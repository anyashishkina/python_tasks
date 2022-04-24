f = open('17-278.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break 
    d.append(int(s))
sm, cnt, min_sum = 0, 0, 100000000
for i in range(len(d)):
    sm += oct(d[i]).count('7') * 7 
for i in range(len(d)-1):
    if (d[i] > sm) and (d[i+1] > sm):
        cnt += 1 
        min_sum = min(min_sum, d[i] + d[i+1])
print(cnt, min_sum)
