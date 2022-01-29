from itertools import permutations 
cmd = list(set(permutations('МАРИНА', 6)))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb[0] in 'АИ':
        return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
