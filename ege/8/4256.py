from itertools import permutations 
cmd = list(permutations('КУСАТЬ', 5))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    k = o
    if ''.join(comb[0]) == 'Ь':
        return False
    if 'СУК' in comb:
        return False
    for i in range(len(comb)-1):
        if comb[i] in cmd:
            k += 1 
            if k > 1:
                return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
