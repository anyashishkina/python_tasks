from itertools import permutations
cmd = list(permutations('ТЬЮРИНГ', 6))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb[0] == 'Ь':
        return False
    for i in range(len(comb) - 1):
        if comb[i] in ['Ю', 'И'] and comb [i+1] == 'Ь':
            return False
    return True
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
