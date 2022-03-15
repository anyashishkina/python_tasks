f = open('17 (8).txt')
d = []
cnt, max_s = 0, 0
while True:
    s = f.readline()
    if s == '':
        break 
    d.append(int(s))
for i in range(len(d)-1):
    if ((d[i] % 160) != (d[i+1] % 160)) and ((d[i] % 7 == 0) or (d[i+1] % 7 == 0)):
        cnt += 1 
        max_s = max(max_s, d[i] + d[i+1])
print(cnt, max_s)
