f = open('24-171.txt').read()
strings = f.split('\n')

cur_len, max_len = 0, 0

for s in strings:
    for i in range(len(s)-2):
        if s[i] == 'X' and s[i+1] == 'Y' and s[i+2] == 'Z':
            cur_len += 3
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1
            max_len = max(max_len, cur_len)

print(max_len)
