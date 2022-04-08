x = (5**300 * 15**100) - (25**50 + 125**100)
s = ''
while x > 0:
    s = str(x%5) + s
    x //= 5
sm = 0
for i in range(len(s)):
    if s[i] != '4':
        sm += int(s[i])
print(sm)
