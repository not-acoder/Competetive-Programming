n = int(input())
lst = []
temp = []
temp1=0
for i in range(n):
    lst.append(input())
print(lst)

set1 = set(lst)
print(set1)
distinct_words = len(set1)
for j in range(distinct_words):
    for k in range(n):
        if(j==k):
            temp1 = temp1 + 1
            temp.append(temp1)
            temp1=0

print(temp)