f = open('24.txt')
s = f.readline()
s = s.replace('AA', '*')
s = s.replace('CC', '*')
cur_len, max_len = 1, 0
for i in range(len(s)-1):
    if s[i] == '*' and s[i+1] == '*':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)
