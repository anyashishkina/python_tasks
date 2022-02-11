def F(ns, nf):
    if ns > nf:
        return 0 
    if ns == nf:
        return 1 
    return F(ns + 1, nf) + F(ns + 2, nf) + F(ns * 2, nf)
print(F(3, 10) * F(10, 12))
