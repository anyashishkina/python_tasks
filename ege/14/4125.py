x = 81**18 - (81**8 - 1) * ((8+1)**8 + 1)//8 - 8
s = ''
while x > 0:
    s = str(x%3) + s
    x //= 3
print(s.count('1'))
