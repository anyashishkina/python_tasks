from itertools import permutations 
cmd = list(permutations('КУСАТЬ', 5))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb[0] == 'Ь':
        return False
    if 'СУК' in ''.join(comb):
        return False
    for i in range(len(comb)-1):
        if comb.count(comb[i]) > 1:
                return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
