'''Необходимо определить максимальное произведение подпоследовательности, состоящей из одного или более идущих подряд элементов.'''

f = open('27A.txt')
n = int(f.readline())
d = [int(x) for x in f]
max_pr = -10000000000000000000000000000
for i in range(n):
    cur_pr = d[i]
    max_pr = max(max_pr, cur_pr)
    for j in range(i+1, n):
        cur_pr *= d[j]
        max_pr = max(max_pr, cur_pr)
print(max_pr)


