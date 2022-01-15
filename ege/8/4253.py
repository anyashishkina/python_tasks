from itertools import permutations
cmd = list(permutations('01234567', 4))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb[0] in [0, 2, 4, 6]:
        return False
    for i in range(len(comb)-1):
        if comb[i] < comb[i+1]:
            return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
#выводит 70
