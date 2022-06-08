s = open('24-208.txt').readline()
m = ''
a = s.split('2022')
for i in range(len(a)-5):
    s1 = a[i] + '2022' + a[i+1] + '2022' + a[i+2] + '2022' + a[i+3] + '2022' + a[i+4]
    m = max(m, s1, key = len)
print(len(m))
