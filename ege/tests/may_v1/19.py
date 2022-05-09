def game(l, r, h):
    if (h == 2) and ((l + r) >= 84):
        return True 
    if (h == 2) and ((l + r) < 84):
        return False
    if (h == 1) and ((l + r) >= 84):
        return False
    h += 1 
    return game(l+1, r, h) or game(l, r+1, h) or game(l*2, r, h) or game(l, r*3, h)
for x in range(1, 67+1):
    if game(16, x, 0):
        print(x)
        break
