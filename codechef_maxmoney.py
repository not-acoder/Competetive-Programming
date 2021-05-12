t=int(input())
#print(t)
for _ in range(t):
    n,b=map(int,input().split())
    #print(n,b)
    lst=list(map(int,input().split()))
    #print(lst)
    if b in lst:
        print(b)
    else:
        #print('hi')
        possible=[]
        for i in range(n):
            if lst[i]<b:
                #print('hello')
                possible.append(lst[i])
                #print(possible)
                sum=lst[i]
                print(sum)
                j=i+1
                while(sum<=b):
                    possible.append(sum)
                    print(possible)
                    if j<n:
                        sum+=lst[j]
                    #except IndexError:
                        #pass
                        j += 1

        print(max(possible))
