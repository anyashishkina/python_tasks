f = open('27_B (1).txt')
n = int(f.readline())
sum_ost = [1096594666] * 43
b = [0] * 43
s_max = 0
l = 0
s = 0
sum_ost[0] = 0
b[0] = -1
for i in range(n):
    x = int(f.readline())
    s += x
    ost = s % 43
    if s - sum_ost[ost] == s_max:
        l = min(l, i - b[ost])
    if s - sum_ost[ost] > s_max:
        s_max = s - sum_ost[ost]
        l = i - b[ost]
    if sum_ost[ost] == 1096594666:
        sum_ost[ost] = s
        b[ost] = i


print(l)
