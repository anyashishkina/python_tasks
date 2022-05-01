f = open('17-271 (1).txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
ave = sum(d) / len(d)
cnt, max_s = 0, 0
for i in range(len(d)-1):
    if ((abs(d[i]) % 10) + (abs(d[i+1]) % 10)) == 7:
        cnt += 1 
        if (d[i] < ave) and (d[i+1] < ave):
            max_s = max(max_s, d[i] + d[i+1])

print(cnt, max_s)  
