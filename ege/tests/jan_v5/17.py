f = open('17 (4).txt')
d = []
cnt, max_s = 0, 0
while True:
    f_cont = f.readline()
    if f_cont == '':
        break
    d.append(int(f_cont))
for i in range(len(d)-2):
    if (d[i]<d[i+1]+d[i+2]) and (d[i+1]<d[i]+d[i+2]) and (d[i+2]<d[i]+d[i+1]):
        if ((d[i]**2-d[i+1]**2-d[i+2]**2)/(-2*d[i+1]*d[i+2]) > 0) and ((d[i+1]**2-d[i]**2-d[i+2]**2)/(-2*d[i]*d[i+2]) > 0) and ((d[i+2]**2-d[i]**2-d[i+1]**2)/(-2*d[i]*d[i+1]) > 0):
            cnt += 1
            max_s = max(max_s, d[i]+d[i+1]+d[i+2])
    else:
        cnt, max_s == 0, 0 
print(cnt, max_s)
