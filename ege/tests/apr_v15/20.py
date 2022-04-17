def game(l, r, h):
    if (h == 3) and (l + r >= 88):
        return True
    if (h == 3) and (l + r < 88):
        return False
    if (h < 3) and (l + r >= 88):
        return False
    h += 1
    if h == 1 or h == 3:
        return game(l+1, r, h) or game(l*3, r, h) or game(l, r+1, h) or game(l, r*3, h)
    if h == 2:
        return game(l+1, r, h) and game(l*3, r, h) and game(l, r+1, h) and game(l, r*3, h)
for x in range(1, 72):
    if game(6, x, 0):
        print(x)
