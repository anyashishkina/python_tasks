def F(ns, nf):
    if ns > nf:
        return 0 
    if ns == nf:
        return 1 
    if ns == 11:
        return 0 
    return F(ns + 1, nf) + F(ns * 2, nf) + F(ns + 5, nf)
print(F(1, 9)*F(9, 18))
