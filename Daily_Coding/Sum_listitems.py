from itertools import combinations
a = [int(x) for x in input().split()]
k = int(input())

comb = combinations(a,2)
chk = False
lst = list(comb)
#print(lst)
for i in lst:
    if (i[0]+i[1]==k):
        chk = True
        break;

print(chk)