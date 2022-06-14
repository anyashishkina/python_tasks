cnt = 0
for i in range(28672, 100000, 2):
    x = oct(i)[2:]
    if len(x) == 5 and x[0] == '7' and (('65' in x and '56' not in x) or ('56' in x and '65' not in x)):
        cnt += 1 
print(cnt)
