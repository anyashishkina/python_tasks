def game(k, h):
    if (h == 2) and (k >= 36) and (k <= 60):
        return True
    if (h == 2) and ((k < 36) or (k > 60)):
        return False
    if (h == 1) and (k >= 36) and (k <= 60):
        return False
    if (h == 1) and (k > 60):
        return True
    h += 1
    if h == 1:
        return game(k + 1, h) and game(k * 2, h) and game(k * 3, h)
    if h == 2:
        return game(k + 1, h) or game(k * 2, h) or game(k * 3, h)

for x in range(1, 35+1):
    if game(x, 0):
        print(x)
        break
        
        
        
def game(k, h):
    if ((h == 2) or (h == 4)) and (k >= 36) and (k <= 60):
        return True
    if (h == 4) and ((k < 36) or (k > 60)):
        return False
    if (h == 2) and (k > 60):
        return False
    if (h < 4) and (k >= 36) and (k <= 60):
        return False
    if ((h == 1) or (h == 3)) and (k > 60):
        return True
    h += 1
    if (h == 1) or (h == 3):
        return game(k + 1, h) and game(k * 2, h) and game(k * 3, h)
    if (h == 2) or (h == 4):
        return game(k + 1, h) or game(k * 2, h) or game(k * 3, h)

for x in range(1, 35+1):
    if game(x, 0):
        print(x)
