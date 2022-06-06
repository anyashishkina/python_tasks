s = open('107_24.txt').readline()
m1 = 'AB'
m2 = 'CB' 
while m1 in s:
    m1 += 'AB'
while m1 not in s:
    m1 = m1[:-1]
while m2 in s:
    m2 += 'AB'
while m2 not in s:
    m2 = m2[:-1]
print(len(m1) + len(m2)
