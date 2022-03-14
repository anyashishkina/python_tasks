x = 2*216**6 + 3*36**9 - 432
cnt = 0
while x > 0:
    if x % 6 == 5:
        cnt += 1 
    x //= 6 
print(cnt)
