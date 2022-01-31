from itertools import product
cmd = list(product('ПСКАЛЬ', repeat = 4))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb[0] == 'Ь':
        return False
    for i in range(len(comb) - 1):
        if comb [i] == 'Ь' and comb [i+1] == 'Ь':
            return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
