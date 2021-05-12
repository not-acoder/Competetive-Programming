n=int(input())
a=[]
prev=1
k=10
while(n!=0):
    rem=n%k
    a.append(rem/prev)
    n-=rem
    k*=10
    prev*=10

if a==a[::-1]:
    print('palindrome')
else:
    print('not palindrome')