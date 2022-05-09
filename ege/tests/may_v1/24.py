text = open('24 (9).txt').read()
strings = text.split('\n')

min_g = 1000000000
string_g = 0 

for s in strings:
    if s.count('G') < min_g:
        min_g = s.count('G')
        string_g = s 

max_a = ''
max_count = 0 
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in a:
    if string_g.count(i) >= max_count:
        max_count = string_g.count(i)
        max_a = i
print(max_a)
