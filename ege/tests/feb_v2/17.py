f = open('17 (6).txt')
d, sum_nech, cnt_nech, cnt, max_s = [], 0, 0, 0, 0
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d)):
    if d[i] % 2 != 0:
        sum_nech += d[i]
        cnt_nech += 1 
    ave = sum_ch / cnt_ch
for i in range(len(d)-1):
    if ((d[i] % 5 == 0) or (d[i+1] % 5 == 0)) and ((d[i] < ave) or (d[i+1] < ave)):
        cnt += 1 
        max_s = max(max_s, d[i] + d[i+1])
print(cnt, max_s)
