f = open('24-157.txt')
s = f.readline()
cnt, max_k = 0, 0
for i in range(len(s)-1):
    if (s[i] == 'P' and s[i+1] == 'R') or (s[i] == 'R' and s[i+1] == 'P'):
        cnt = 1
    else:
        cnt += 1
        max_k = max(max_k, cnt)
print(max_k)
