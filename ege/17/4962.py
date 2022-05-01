f = open('17-274.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
cnt, min_s = 0, 100000000 
for i in range(len(d)-1):
    if (abs(d[i]) + abs(d[i+1]) > 17043) and ((abs(d[i]) + abs(d[i+1])) % 3 == 0):
        cnt += 1 
        min_s = min(min_s, d[i] + d[i+1])
print(cnt, min_s)
