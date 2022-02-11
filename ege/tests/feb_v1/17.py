f = open('17 (5).txt')
d, sum_ch, cnt_ch, cnt, max_s = [], 0, 0, 0, 0
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d)-1):
    if d[i] % 2 == 0:
        sum_ch += d[i]
        cnt_ch += 1 
    ave = sum_ch / cnt_ch
    if ((d[i] % 3 == 0) or (d[i+1] % 3 == 0)) and ((d[i] < ave) or (d[i+1] < ave)):
        cnt += 1 
        max_s = max(max_s, d[i] + d[i+1])
print(cnt, max_s)
