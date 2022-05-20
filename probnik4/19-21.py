def game(l, r, h):
    if (h == 2) and ((l+r)>=45):
        return True
    if (h == 2) and ((l+r)<45):
        return False
    if (h == 1) and ((l+r)>=45):
        return False
    h += 1
    return game(l + r, r, h) or game(l, r+l, h)

for x in range(100):
    if game(7, x, 0):
        print(x)
        break
