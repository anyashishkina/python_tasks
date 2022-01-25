x = 49**7 + 7**20 - 28
cnt = 0
while x > 0:
    if x % 7 == 6:
        cnt += 1 
    x //= 7
print(cnt)
