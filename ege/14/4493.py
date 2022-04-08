x = 1*3**37 + 2*3**23 + 3*3**20 + 4*3**4 + 5*3**3 + 4 + 5
s = ''
while x > 0:
    s = str(x%9) + s
    x //= 9
for i in range(len(s)):
    if s[i] != '0':
        print(s[i:].count('0'))
        break
