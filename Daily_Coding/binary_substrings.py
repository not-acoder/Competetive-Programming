def validate(s):
    count=0
    for i in range(len(s)-1):
        counter = [0, 0]
        if s[i] == '0':
            counter[0] += 1
        elif s[i] == '1':
            counter[1] += 1
        for j in range(i+1,len(s)):
            counter[int(s[j])]+=1
            if s[i]!=s[j]:
                if counter[0]==counter[1]:
                    count+=1
                    break
                elif  j!=len(s)-1 and s[j]!=s[j+1]:
                    break
            elif s[i]==s[j]:
                pass
    print(count)


n='1101000100010101101000011'
validate(n)

