from itertools import product
cmd = list(product('СТЕПУХА', repeat = 4))
cnt = 0
for i in range(1000, len(cmd)):
    c = ''.join(cmd[i])
    k = 0
    for j in range(len(c)-1):
        if c[j] != c[j+1]:
            k += 1 
        if k == 3:
            cnt += 1 
print(cnt)
