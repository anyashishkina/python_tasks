from math import *
for n in range(9990000, 10000000):
    div = set()
    for d in range(2, int(sqrt(n))-1):
        if n % d == 0:
            div.add(d)
            div.add(n//d)
    if len(div) == 0:
        print(n)
        
        
from math import *
for n in range(10000000, 11111000):
    div = set()
    for d in range(2, int(sqrt(n))-1):
        if n % d == 0:
            div.add(d)
            div.add(n//d)
    if len(div) == 0:
        print(n)
