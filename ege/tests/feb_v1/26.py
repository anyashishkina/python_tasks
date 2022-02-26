f = open('26 (2).txt')
a = f.readline()
cnt, max_d = 0, 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if (i % 2 != 0) and (j % 2 != 0):
            ave = (i + j) / 2
            if str(ave) in a:
                cnt += 1
                max_d = max(ave, max_d)
print(cnt, max_d)
