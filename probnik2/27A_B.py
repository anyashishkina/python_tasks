f = open('27-59a.txt')
n = int(f.readline())
d = [int(x) for x in f]
sm, cnt = 0, 0 
for i in range(n-1):
  sm = d[i] 
  for j in range(i+1, n):
    sm += d[j]
    if sm % 10 == 5:
      cnt += 1 
print(cnt)
