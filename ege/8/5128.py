cnt = 0
for i in range(1048576, 17000000):
    x = hex(i)[2:]
    if len(x) == 6 and x[0] != '1' and x[-1] == 'b' and x[-2] == 'a':
        cnt += 1 
print(cnt)
