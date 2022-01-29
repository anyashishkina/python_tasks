f = open('17 (2).txt')
d = []
cnt, max_d = 0, 0
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d) - 1):
    if (d[i] - d[i+1])% 80 == 0:
        cnt += 1 
        max_d = max(max_d, abs(d[i] - d[i+1]))
print(cnt, max_d)
