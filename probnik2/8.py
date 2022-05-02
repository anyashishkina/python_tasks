slovo = 'ПСКАЛЬ'
n = 0
for s1 in range(len(slovo)):
  for s2 in range(len(slovo)):
    for s3 in range(len(slovo)):
      for s4 in range(len(slovo)):
        s = slovo[s1] + slovo[s2] + slovo[s3] + slovo[s4] 
        for i in range(len(s)-1):
          if (s[0] != 'Ь') and (s[i] != 'Ь') and (s[i+1] != 'Ь'):
            n += 1
print(n)
