def F(n):
    print(n)
    if n < 4:
        F(n + 1)
        F(n + 3)
print(F(1))
