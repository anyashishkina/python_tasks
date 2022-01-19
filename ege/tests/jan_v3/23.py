def F(ns, nf):
    if ns > nf:
        return 0 
    if ns == nf:
        return 1
    if ns == 14:
        return 0 
    return F(ns + 1, nf) + F(ns + 2, nf)
    
print(F(2, 9)*F(9, 18))
