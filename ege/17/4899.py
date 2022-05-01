f = open('17-272.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
cnt, sm = 0, 0
for i in range(len(d)):
    if d[i] > 0:
        cnt += 1 
        sm += d[i]
ave = sm / cnt
cnt2, max_s = 0, 0
for i in range(len(d)-1):
    if (d[i] > ave) or (d[i+1] > ave):
        cnt2 += 1
        s1 = str(abs(d[i]))
        s2 = str(abs(d[i+1]))
        sm1, sm2 = 0, 0
        for i in range(len(s1)):
            sm1 += int(s1[i])
        for i in range(len(s2)):
            sm2 += int(s2[i])
        max_s = max(sm1, sm2)

print(cnt2, max_s)
