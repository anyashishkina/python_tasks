def F(ns, nf):
    if ns > nf:
        return 0
    if ns == nf:
        return 1 
    return F(ns + 1, nf) + F(ns * 3, nf) + F(ns + 2, nf)
print(F(1, 10)*F(10, 12)*F(12, 15))
