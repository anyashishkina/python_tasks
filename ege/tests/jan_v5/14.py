x = 9**11 * 3**20 - 3**9 - 27
cnt = 0 
while x > 0:
    if x % 3 == 2:
        cnt += 1 
    x //= 3 
print(cnt)
