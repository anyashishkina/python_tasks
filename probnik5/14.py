x = 5*216**1256 - 5*36**1146 + 4*6**1053 - 1087
s = ''
while x > 0:
    s = str(x%6) + s
    x //= 6
sm = 0
for i in range(len(s)):
    sm += int(s[i])
print(sm)
