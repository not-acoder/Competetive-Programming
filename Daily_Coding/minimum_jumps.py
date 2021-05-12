def minjumps(a):
    n=len(a)
    ways=[float("inf") for i in range(n)]
    ways[0]=0
    for i in range(n):
        if a[i]==0:
            pass
        for j in range(i+1,i+1+a[i]):
            try:
                ways[j]=min(ways[j],ways[j-a[i]]+1)
            except IndexError:
                pass
    return ways[-1]

result=minjumps([2,1])
print(result)