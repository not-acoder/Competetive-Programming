T=int(input())
i=0
for i in range(T):
    s=input()
    if len(set(s))==3:
        print('YES')
    else:
        print('NO')