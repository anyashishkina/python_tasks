from itertools import product
cmd = list(product('01234567', repeat = 4))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    for i in range(len(comb)):
        if int(''.join(comb[i]), base = 8) % 4 != 0:
            return False
    return True
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
