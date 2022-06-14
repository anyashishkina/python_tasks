from itertools import product
cmd = list(product('ПОЛЯКВ', repeat = 4))
def is_right(comb):
    k = 0
    s = 'ВОЛК'
    for i in range(len(s)):
        for j in range(len(comb)):
            if (i == j) and (s[i] == comb[j]):
                k += 1 
    if k > 2:
        return False
    if k < 2:
        return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
