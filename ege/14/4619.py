x = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
s = ''
while x > 0:
    if x%15 == 10:
        s = 'a' + s
    elif x%15 == 11:
        s = 'b' + s
    elif x%15 == 12:
        s = 'c' + s
    elif x%15 == 13:
        s = 'd' + s
    elif x%15 == 14:
        s = 'e' + s
    else:
        s = str(x%15) + s
    x//=15
sm = 0
for i in range(10):
    if str(i) in s:
        sm += 1
a = ['a', 'b', 'c', 'd', 'e']
for i in range(len(a)):
    if a[i] in s:
        sm += 1
print(sm)
