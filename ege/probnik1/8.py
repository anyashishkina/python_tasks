slovo = 'ЩОГБА'
n = 0
for s1 in range(len(slovo)):
    for s2 in range(len(slovo)):
        for s3 in range(len(slovo)):
            for s4 in range(len(slovo)):
                for s5 in range(len(slovo)):
                    for s6 in range(len(slovo)):
                        s = slovo[s1]+slovo[s2]+slovo[s3]+slovo[s4]+slovo[s5]+slovo[s6]
                        n += 1
                        if s == 'ОБЩАГА':
                            print(n)
