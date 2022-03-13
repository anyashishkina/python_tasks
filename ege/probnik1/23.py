def F(ns, nf):
    if ns == nf:
        return 1 
    if ns > nf:
        return 0 
    return F(ns + 1, nf) + F(ns + 2, nf)
print(F(11, 29))
