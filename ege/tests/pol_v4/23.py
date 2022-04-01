def F(ns, nf):
    if ns == nf:
        return 1 
    if ns > nf:
        return 0 
    return F(ns + 3, nf) + F(ns * 3, nf)
cnt = 0 
for nf in range(2, 100, 2):
    if F(3, nf) != 0:
        cnt += 1 
print(cnt)
