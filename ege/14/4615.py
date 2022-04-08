x = 12**34 + 7*12**26 - 3*12**16 + 2*12**5 + 552
s = ''
while x > 0:
    if x%12 == 10:
        s = 'a' + s
    if x%12 == 11:
        s = 'b' + s
    s = str(x%12) + s
    x //= 12
cnt = 0
for i in range(10):
    if str(i) in s:
        cnt += 1
a = ['a', 'b']
for i in range(len(a)):
    if a[i] in s:
        cnt += 1
print(cnt)
