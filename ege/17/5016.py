f = open('17-277.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
sm = 0 
for i in range(len(d)):
    if d[i] % 60 == 0:
        x = abs(d[i])
        s = ''
        while x > 0:
            s = str(x % 3) + s 
            x //= 3
        sm += 2 * s.count('2')
cnt, max_s = 0, 0 
for i in range(len(d)-1):
    if (d[i] > sm) or (d[i+1] > sm):
        cnt += 1 
        max_s = max(max_s, d[i] + d[i+1])
print(cnt, max_s)
