x = 16**44 * 16**30 - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))
s = hex(x)[2:]
s = s.replace('f', '0')
for i in range(len(s)):
    if s[i] != '0':
        print(s[i:].count('0')-3)
        break
