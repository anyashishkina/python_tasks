x = (16**25 + 4**10) - (16**20 + 32**3)
s = ''
while x > 0:
    s = str(x%4) + s
    x //= 4
s = s[::-1]
for i in range(len(s)):
    if s[i] == '2':
        print(i)
