f = open('17-292.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
cnt, min_sum =0, 1000000000
for i in range(len(d)-1):
    if abs(d[i]%17 - d[i+1]%17) == d[i]%4 + d[i+1]%4:
        cnt += 1
        min_sum = min(min_sum, d[i] + d[i+1])
print(cnt, min_sum)
