f = open('17.txt')
d = []
cnt, s, max_s = 0, 0, 0
while True:
    f_cont = f.readline()
    if f_cont == '':
        break
    d.append(int(f_cont))
for i in range(len(d) - 2):
    if (d[i]**2 == d[i+1]**2 + d[i+2]**2) or (d[i+1]**2 == d[i]**2+d[i+2]**2) or (d[i+2]**2 == d[i]**2 + d[i+1]**2):
        cnt += 1
        s = d[i] + d[i+1] + d[i+2]
        max_s = max(max_s, s)
print(cnt, max_s)
