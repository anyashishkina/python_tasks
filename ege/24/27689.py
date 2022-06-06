s = open('24_demo (4).txt').readline()
s = s.replace('XYZ', '*')
max_len, cur_len =0, 0
for i in range(len(s)):
    if s[i] == '*':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
        
print(max_len)
