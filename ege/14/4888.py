x = 49**129 + 7**131 - 2
s = ''
while x > 0:
    s = str(x % 7) + s
    x //= 7
ms = 0
for i in range(len(s)):
    if int(s[i]) > int(ms):
        ms = s[i]
s = s.replace('0', ms)
print(s.count(ms))
