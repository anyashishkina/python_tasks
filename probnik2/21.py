def game(l, s, r, h):
    if ((h == 2) or (h == 4)) and ((l + s + r) >= 73):
        return True
    if (h == 4) and ((l + s + r) < 73):
        return False
    if (h < 4) and ((l + s + r) >= 73):
        return False
    h += 1 
    if (h == 1) or (h == 3):
        return game(l+3,s,r,h) and game(l+13,s,r,h) and game(l+23,s,r,h) and game(l,s+3,r,h) and game(l,s+13,r,h) and game(l,s+23,r,h) and game(l,s,r+3,h) and game(l,s,r+13,h) and game(l,s,r+23,h)
    if (h == 2) or (h == 4):
        return game(l+3,s,r,h) or game(l+13,s,r,h) or game(l+23,s,r,h) or game(l,s+3,r,h) or game(l,s+13,r,h) or game(l,s+23,r,h) or game(l,s,r+3,h) or game(l,s,r+13,h) or game(l,s,r+23,h)
for x in range(1, 23+1):
    if game(2, x, 2*x, 0):
        print(x)
