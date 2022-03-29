t = sorted ('И,Н,С,Т,А,В,К'.split(','))
a = []
for x1 in t:
    for x2 in t:
        for x3 in t:
            for x4 in t:
                if x1 in 'НСТВК' and x4 in 'ИА':
                    a.append(x1+x2+x3+x4)
print(a.index('НИКА')+1)
