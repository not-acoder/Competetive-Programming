def validate(a):
    for i in range(len(a)-1):
        if (a[i]=='b' and a[i+1]=='a') or (a[i]=='c' and a[i+1]=='b'):
            return False;
            break

    return True


def smallestString(s):
    t = list(s)
    flag = False
    r=''
    while (flag==False):
        for i in range(len(s) - 1):
            if t[i] == 'b' and t[i+1] == 'a':
                t[i], t[i + 1] = t[i + 1], t[i]
            elif t[i] == 'c' and t[i+1] == 'b':
                t[i], t[i + 1] = t[i + 1], t[i]

        flag = validate(t)
    for k in t:
        r+=k
    return r

s = input()
answer=smallestString(s)
print(answer)