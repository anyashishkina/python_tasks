f = open('27-15Axt')
n, k = map(int,(f.readline().split()))
d = [int(x) for x in f]
max_sum = -1000000000000000 
for i in range(n-1):
  cnt = 0 
  if d[i] < 0 and abs(d[i]) % 10 == 3:
    cur_sum = d[i] 
    cnt += 1 
  else:
    cur_sum = d[i]
  for j in range(i+1, n):
    if d[j] < 0 and abs(d[j])%10 == 3:
      cnt += 1 
    if cnt == 4:
      break 
    cur_sum += d[j]
    max_sum = max(max_sum, cur_sum)
print(max_sum)


