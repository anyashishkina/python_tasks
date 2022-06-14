cnt = 0
for i in range(983040, 3000000):
    x = hex(i)[2:]
    if len(x) == 5 and x[0] == 'f' and x[-1] == 'a' and x.count('3b')==1:
        cnt += 1 
print(cnt)
