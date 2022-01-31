from itertools import permutations
cmd = list(set(permutations('ТИКТОК', 6)))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    for i in range(len(comb) - 1):
        if comb[i] == comb [i+1]:
            return False
    return True
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
