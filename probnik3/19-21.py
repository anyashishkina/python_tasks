def game(k, h):
    if (h == 2) and (k >= 65) and (k <= 100):
        return True
    if (h == 2) and ((k < 65) or (k > 100)):
        return False
    if (h == 1) and (k >= 65) and (k <= 100):
        return False
    if (h == 1) and (k > 100):
        return True
    h += 1
   return game(k +1, h) or game(k * 3, h)
    
for x in range(1, 64+1):
    if game(x, 0):
        print(x)
        break
        
        
        
def game(k, h):
    if (h == 3) and (k >= 65) and (k <= 100):
        return True
    if (h == 3) and ((k < 65) or (k > 100)):
        return False
    if (h == 1) and (k > 100):
        return False
    if (h < 3) and (k >= 65) and (k <= 100):
        return False
    if (h == 2) and (k > 100):
        return True
    h += 1
    if (h == 1) or (h == 3):
        return game(k +1, h) or game(k * 3, h)
    if (h == 2):
         return game(k +1, h) and game(k * 3, h)
        
    
for x in range(1, 64+1):
    if game(x, 0):
        print(x)
        
        
        
        
        
        
 def game(k, h):
    if ((h == 2) or (h == 4)) and (k >= 65) and (k <= 100):
        return True
    if (h == 4) and ((k < 65) or (k > 100)):
        return False
    if (h == 2) and (k > 100):
        return False
    if (h < 4) and (k >= 65) and (k <= 100):
        return False
    if ((h == 1) or (h == 3)) and (k > 100):
        return True
    h += 1
    if (h == 1) or (h == 3):
        return game(k +1, h) and game(k * 3, h)
    if (h == 2) or (h == 4):
         return game(k +1, h) or game(k * 3, h)
        
    
for x in range(1, 64+1):
    if game(x, 0):
        print(x)
        
