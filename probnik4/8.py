slovo = 'ВАЙФУ'
cnt = 0
for s1 in range(len(slovo)):
    for s2 in range(len(slovo)):
        for s3 in range(len(slovo)):
            for s4 in range(len(slovo)):
                s = slovo[s1] + slovo[s2] + slovo[s3] + slovo[s4]
                if (s[0] != 'Й') and ('ВФ' not in s) and ('ФВ' not in s):
                    cnt += 1
print(cnt)
