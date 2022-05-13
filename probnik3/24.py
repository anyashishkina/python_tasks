f = open('24-178.txt')
s = f.readline()
s = s*2
cur_len, max_len = 1, 0
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
        max_len = max(max_len, cur_len)
print(max_len)
