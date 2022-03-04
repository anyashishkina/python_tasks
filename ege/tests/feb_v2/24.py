f = open('24 (3).txt')
f_cont = f.read()
s = f_cont.split('\n')
len_str = 0
max_n = 100000000000
for i in range(len(s)-1):
    if s[i].count('N') < max_n:
        max_n = s[i].count('N')
        len_str = i
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter= ''
cnt_letter = 0
for i in alp:
    if cnt_letter <= s[len_str].count(i):
        cnt_letter = s[len_str].count(i)
        letter = i

print(letter)
print(len_str)
