f = open('17-5.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
cnt, max_s =0, 0
for i in range(len(d)-1):
    if (abs(d[i]) % 10 == 7) or (abs(d[i+1]) % 10 == 7):
        cnt += 1 
        max_s = max(max_s, d[i] + d[i+1])
print(cnt, max_s)
