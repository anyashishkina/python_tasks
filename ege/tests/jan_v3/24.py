f = open('24_demo.txt')
s = f.readline()
max_l, cnt = 0, 0
for i in range(1, len(s) - 1):
    if s[i] != s[i+1]:
        cnt += 1 
        if cnt > max_l:
            max_l = cnt 
    else:
        cnt = 1 
print(max_l)
