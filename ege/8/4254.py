from itertools import permutations
cmd = list(permutations('01234', 5))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    k = 0 
    for i in range(len(comb)):
        if comb[i] in [1,3]:
            k += 1 
        if k > 3:
            return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
#выводит 120
