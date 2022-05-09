f = open('17 (13).txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break 
    d.append(int(s))
cnt, max_s = 0, 0
for i in range(len(d)-2):
    a = sorted([d[i], d[i+1], d[i+2]])
    if a[2]**2 < (a[1]**2 + a[0]**2):
        cnt += 1 
        max_s = max(max_s, sum(a))
print(cnt, max_s)
