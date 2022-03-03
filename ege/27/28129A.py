f = open('28129_A.txt')
m1_7, m2_7, m1, m2 = 0, 0, 0, 0
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d)):
    if (d[i] % 7 == 0) and (d[i] > m1_7):
        m1_7 = d[i]
    if (d[i] % 7 != 0) and (d[i] > m2_7) and (d[i] % 160 != m1_7 % 160):
        m2_7 = d[i]
    if (d[i] % 7 == 0) and (d[i] > m1) and (d[i] != m1_7):
        m1 = d[i]
    if (d[i] % 7 != 0) and (d[i] > m2) and (d[i] % 160 != m1 % 160):
        m2 = d[i]
if m1_7 + m2_7 > m1 + m2:
    print(m1_7, m2_7)
else:
    print(m1, m2)
