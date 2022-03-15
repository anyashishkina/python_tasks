def F(ns, nf):
    if ns == nf:
        return 1 
    if ns > nf:
        return 0 
    if ns == 33:
        return 0 
    return F(ns + 1, nf) + F(ns * 2, nf) + F(ns * 3, nf)
print(F(3, 15)*F(15, 50))
