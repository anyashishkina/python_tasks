x = (7**160 * 7**90) - (14**150 + 2**13)
s = ''
while x > 0:
    s = str(x%7) + s
    x //= 7
sm = 0
for i in range(len(s)):
    if s[i] != '6':
        sm += int(s[i])
print(sm)
