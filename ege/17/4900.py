f = open('17-273.txt')
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
mx = max(d)
cnt = 0 
for i in range(len(d)-2):
    if (d[i] + d[i+1] + d[i+2]) < mx:
        cnt += 1
print(cnt, max(d) + min(d)) 
