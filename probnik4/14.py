x = 4**503 + 3 * 4**244 - 2 * 4**444 - 95
cnt = 0
while x > 0:
    if x % 4 == 3:
        cnt += 1
    x //= 4
print(cnt)
                    

