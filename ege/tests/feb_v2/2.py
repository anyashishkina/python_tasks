print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (not z) and x 
            if f == True:
                print(x, y, z)
