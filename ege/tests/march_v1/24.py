f = open('24 (1).txt')
s = f.read().split('\n')
k = 0
for i in range(len(s)):
    if s[i].count('E') > s[i].count('A'):
        k += 1
print(k)
