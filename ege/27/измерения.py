'''Набор данных представляет собой результаты измерений, выполняемые прибором с интервалом 1 минута. 
Требуется найти для этой последовательности контрольное значение - наименьшую сумму квадратов двух измерений, выполненных с интервалом не менее, чемв 5 минут.'''

f = open('27A.txt')
n = int(f.readline())
d = [int(x) for x in f]
min_sum = 100000000000000
for i in range(n-5):
    for j in range(i+5, n):
        min_sum = min(min_sum, d[i]**2 + d[j]**2)
print(min_sum)



f = open('27B.txt')
n = int(f.readline())
d = [int(x) for x in f]
min1, min2, ind1, ind2 = 1000000, 1000000, 0, 0
for i in range(n):
    if d[i] < min1:
        min1 = d[i]
        min2 = min1 
        ind1 = i
        ind2 = ind1
    elif d[i] < min2:
        min2 = d[i] 
        ind2 = i
print(min1**2 + min2**2)
