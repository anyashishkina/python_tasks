from itertools import product
cmd = list(product('АИКЛМНЬ', repeat = 6))
for i in range(len(cmd)):
    c = ''.join(cmd[i])
    if c[0]=='К' and c[-1]=='Ь':
        if c.count('А')==1 and c.count('И')==1 and c.count('Л')==1 and c.count('М')==1:
            if c[::-1] == ''.join(cmd[i+26655]):
                print(i)
