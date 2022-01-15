from itertools import permutations
cmd = list(permutations('ЗЕРКАЛО', 6))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    k1 = 0 
    k2 = 0
    for i in range(len(comb)-1):
        if comb[i] == 'К':
            k1 += 1 
        if k1 > 4:
            return False
        if comb[i] in comb:
            k2 += 1 
        if k2 > 1:
            return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
