f = open('24.txt')
s = f.readline()
k, max_l = 0, 0
for i in range(1, len(s)-3):
    if s[i] == 'X' and s[i+1] == 'Z' and s[i+2] == 'Z' and s[i+3] == 'Y':
        k = 0
        k += 3
    else:
        k += 1
        max_l = max(max_l, k)
print(max_l)
    
