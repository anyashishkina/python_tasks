from itertools import product
cmd = list(product('ЗЕРКАЛО', repeat = 6))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb.count('К') > 4:
        return False
    for i in range(len(comb)):
        if comb.count(comb[i]) > 1:
           return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
