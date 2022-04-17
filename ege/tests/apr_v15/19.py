def game(l, r, h):
    if (h == 2) and (l + r >= 88):
        return True
    if (h == 2) and (l + r < 88):
        return False
    if (h == 1) and (l + r >= 88):
        return False
    h += 1
    return game(l+1, r, h) or game(l*3, r, h) or game(l, r+1, h) or game(l, r*3, h)
    
for x in range(1, 72):
    if game(6, x, 0):
        print(x)
        break
