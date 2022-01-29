f = open('zadanie24_2.txt')
s = f.readline()
max_l = 0
s1 = 'LDR'
for i in range(1, 100):
    s2 = s1*i
    if s2 in s:
        max_l = i
print(max_l)
