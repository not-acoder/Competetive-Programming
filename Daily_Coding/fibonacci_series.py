n=int(input())
a0=0
a1=1
for i in range(1,n+1):
    print(a0)
    next=a0+a1
    a0=a1
    a1=next