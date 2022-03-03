f = open('27985_A (1).txt')
m14, m2, m7, max_m = 0, 0, 0, 0
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d)):
    if (d[i] % 2 == 0) and (d[i] % 7 != 0) and (d[i] > m2):
        m2 = d[i]
    if (d[i] % 7 == 0) and (d[i] % 2 != 0) and (d[i] > m7):
        m7 = d[i]
    if (d[i] % 14 == 0) and (d[i] > m14):
        m14 = d[i]
    if (d[i] > max_m) and (d[i] != m14):
        max_m = d[i]
if m2 * m7 > m14 * max_m:
    print(m2*m7)
else:
    print(m14*max_m)
