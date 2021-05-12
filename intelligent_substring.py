def longest(s,q,k):

    ref=ord('a')
    ans=0
    i=0

    while(i<len(s)):
        j=i+1
        count=0
        if q[ord(s[i])-ref]=='0':
            count+=1

        Max=1

        while(count<=k):
            #print('count =',count)
            #print(Max)
            if j==len(s):
                break
            if q[ord(s[j])-ref]=='0':
                count+=1
            if count<=k:
                j+=1
                Max+=1

        ans=max(ans,Max)

        i+=1
    return ans


P = 'abcdebdac'
Q = '01111001111111111011111111'
K=0
result=longest(P,Q,K)
print(result)