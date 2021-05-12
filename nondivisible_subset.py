from collections import Counter


def nonDivisibleSubset(k, s):
    len1=0
    for i in range(len(s)):
        s[i] = s[i] % k

    #s.sort(key=Counter(s).get)
    st = set(s)
    try:
        for j in range(len(st)):
            for l in range(j+1,len(st)):
                if(st[j]+st[l]==k or st[j]+st[l]==0):
                    if(s.count(j)>s.count(i) and k/2!=j):
                        len1+=s.count(i)
                    elif(k/2==j):
                        len1+=1


                    if (s.count(j) < s.count(i) and k / 2 != i):
                        len1 += s.count(j)
                    if (k/2 == i):
                        len1 += 1

    except:
        pass;
    return len(s)-len1




if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(result)
