cnt = 0
def F(n):
    global cnt 
    if n > 0:
        cnt += 1 
        F(n - 1)
        F(n // 3)

F(6)
print(cnt)
