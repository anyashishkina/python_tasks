def F(ns, nf):
    if ns == nf:
        return 1
    if ns > nf:
        return 0
    return F(int(bin(ns)[2:]) + 1, nf) + F(int('1' + bin(ns)[2:]), nf)
print(F(4, 49))
