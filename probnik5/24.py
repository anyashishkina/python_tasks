f = open('24-171.txt').read()
strings = f.replace('\n', '')

cur_len, max_len = 1, 0

for s in strings:
    s = s.replace('XYZ', '*')
    for i in range(len(s)):
        if s[i] == '*':
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1
            max_len = max(max_len, cur_len)

print(max_len)
