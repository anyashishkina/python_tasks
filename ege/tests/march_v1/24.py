f = open('24.txt')
s = f.read().split('\n')
k = 0
for i in s:
    if s.count('E') > s.count('A'):
        k += 1
print(k)
