from itertools import permutations
cmd = list(permutations('СОТКАПЛЗ', 5))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb[4] in ['О, А']:
        return False
    if 'ЗЛО'in ''.join(comb):
        return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
