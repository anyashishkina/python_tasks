f = open('27991_A.txt')
m17, m_ch1, m_ch2, m_nech1, m_nech2, s1, s2 = 0, 0, 0, 0, 0, 0, 0
d = []
while True:
    s = f.readline()
    if s == '':
        break
    d.append(int(s))
for i in range(len(d)):
    if (d[i] % 2 == 0) and (d[i] > m_ch1) and (d[i] != m_ch2):
        m_ch1 = d[i]
    if (d[i] % 2 == 0) and (d[i] > m_ch2) and (d[i] != m_ch1):
        m_ch2 = d[i]
    if (d[i] % 2 != 0) and (d[i] > m_nech1) and (d[i] != m_nech2):
        m_nech1 = d[i]
    if (d[i] % 2 != 0) and (d[i] > m_nech2) and (d[i] != m_nech1):
        m_nech2 = d[i]
    if (m_ch1 % 17 == 0) or (m_ch2 % 17 == 0):
        s1 = m_ch1 + m_ch2
    if (m_nech1 % 17 == 0) or (m_nech2 % 17 == 0):
        s2 = m_nech1 + m_nech2
if s1 > s2:
    print(m_ch1, m_ch2)
else:
    print(m_nech1, m_nech2)
