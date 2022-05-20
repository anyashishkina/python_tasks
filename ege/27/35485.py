f = open('27-A (5).txt')
n = int(f.readline())
a = [int(x) for x in f]
ans = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (a[i] + a[j] +a[k]) % 3 == 0:
                ans.append(a[i] + a[j] +a[k])
print(max(ans))
            

    
    
f = open('27-B (3).txt')
n = int(f.readline())
m = [ [] for i in range(3)]
for i in range(n):
    x = int(f.readline())
    m[x%3] += [x]

a = []
for i in range(3):
    m[i].sort()
    a += m[i][-3:]

ans = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if (a[i] + a[j] + a[k]) % 3 == 0:
                ans.append(a[i] + a[j] + a[k])
print(max(ans))
