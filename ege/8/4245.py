from itertools import product
cmd = list(product('СОЛНЦЕ', repeat = 6))
cmd2 = [list(c) for c in cmd]
def is_right(comb):
    if comb.count('О') > 2:
        return False
    if comb.count('Ц') > 1:
        return False
    if comb.count('Ц') == 0:
        return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
