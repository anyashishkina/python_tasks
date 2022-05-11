f = open('27B.txt')
n = int(f.readline())
d = [int(x) for x in f]
ost, cnt = [0] * 12, 0
for x in d:
  if x % 12 == 0:
    cnt += ost[0]
  else:
    cnt += ost[12 - x % 12]
  ost[x % 12] += 1
print(cnt)
