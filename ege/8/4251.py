from itertools import product
cmd = list(product('ЗЕРКАЛО', repeat = 6))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    k = 0 
    k2 = 0
    for i in range(len(comb)-1):
        if comb[i] == 'К':
            k = comb.count('К') 
            if k > 4:
                return False
        if comb.count(comb[i]) > 1:
           return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
