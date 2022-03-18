for n in range(500000, 500100):
    div = []
    for d in range(2, n):
        if n % d == 0:
            div.append(d)
    for i in range(len(div)):
        if (div[i] % 10 == 8) and (div[i] != 8) and (div[i] != n):
            print(n, div[i])
            
