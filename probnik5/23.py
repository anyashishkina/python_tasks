def F(ns, nf):
    if ns == nf:
        return 1
    if ns > nf:
        return 0
    return F(ns * 2, nf) + (ns * 2 + 1, nf)
k = 0
for nf in range(2, 1000):
    if F(1, nf) == 15:
        k += 1
print(k)
    
