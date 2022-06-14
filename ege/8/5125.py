from itertools import product
cmd = list(product('ОГЭИНФ', repeat = 4))
def is_right(comb):
    if comb[0] in 'ГИНФ':
        return False
    if comb[-1] in 'ОГЭИН':
        return False
    if comb[-2] in 'ОГЭИФ':
        return False
    if ''.join(comb).count('ИГ') == 0:
        return False
    if ''.join(comb).count('ОГЭ') > 0:
        return False
    return True 
result = []
for c in cmd:
    if is_right(c):
        result.append(c)
print(len(result))
