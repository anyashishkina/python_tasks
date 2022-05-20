text = open('24-s1.txt').read()
strings = text.split('\n')


min_a = 1000000
string_a = ''

for s in strings:
    if s.count('A') < min_a:
        min_a = s.count('A')
        string_a = s

max_l = ''
max_count = 0
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in a:
    if string_a.count(i) >= max_count:
        max_count = string_a.count(i)
        max_l = i

print(i, max_count)
