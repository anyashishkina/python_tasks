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

        
        
def game(l, r, h):
    if (h == 3) and ((l+r)>=45):
        return True
    if (h == 3) and ((l+r)<45):
        return False
    if (h < 3) and ((l+r)>=45):
        return False
    h += 1
    if (h == 1) or (h == 3):
        return game(l + r, r, h) or game(l, r+l, h)
    if h == 2:
        return game(l + r, r, h) and game(l, r+l, h)

for x in range(100):
    if game(6, x, 0):
        print(x)
        
        
def game(l, r, h):
    if ((h == 2) or (h == 4)) and ((l+r)>=45):
        return True
    if (h == 4) and ((l+r)<45):
        return False
    if (h < 4) and ((l+r)>=45):
        return False
    h += 1
    if (h == 2) or (h == 4):
        return game(l + r, r, h) or game(l, r+l, h)
    if (h == 1) or (h == 3):
        return game(l + r, r, h) and game(l, r+l, h)

for x in range(100):
    if game(x, x, 0):
        print(x)
        break
        
