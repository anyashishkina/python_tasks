def game(n, h):
    if h == 3 and n >= 50 and n <= 70:
        return True
    if h == 3 and (n < 50 or n > 70):
        return False
    if h < 3 and n >= 50 and n <= 70:
        return False
    h += 1
    if h == 1 or h == 3:
        return game(n+1,h) or game(n*2, h)
    if h == 2:
        return game(n+1,h) and game(n*2, h)

for x in range(1, 50):
    if game(x, 0):
        print(x)
