def F(n):
    if n < 2:
        return 1
    if (n >= 2) and (n % 3 == 0):
        return F(n//3) + 1
    if (n >= 2) and (n % 3 != 0):
        return F(n-2) + 5
for n in range(4000, 6000):
    if F(n) == 73:
        print(n)
        break
