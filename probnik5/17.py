f = open('17-10.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
cnt = 0
c = []
for i in range(len(d)-2):
    if (d[i]**2 == d[i+1]**2 + d[i+2]**2) or (d[i+1]**2 == d[i]**2 + d[i+2]**2) or (d[i+2]**2 == d[i]**2 + d[i+1]**2):
        cnt += 1
        c.append(max(d[i], d[i+1], d[i+2]))
print(cnt, sum(c))
    
