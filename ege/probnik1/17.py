f = open('17-202.txt')
d = []
cnt, max_s =0, 0 
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d)-2):
    if ((d[i]<100) or (d[i]>999) or (d[i]%100!=12)) and (d[i+1]>99) and (d[i+1]<1000) and (d[i+1]%100==12) and ((d[i+2]<100) or (d[i+2]>999) or (d[i+2]%100!=12)):
        cnt += 1 
        max_s = max(max_s, d[i] + d[i+1] + d[i+2])
print(cnt, max_s)
