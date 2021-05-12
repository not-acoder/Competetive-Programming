def until_index(r, len2, arr):
    prod1 = prod2 = 1
    for k in range(int(r)):
        prod1 = prod1 * arr[k]

    for l in range(j + 1, len2):
        prod2 *= arr[l]

    final_prod = prod2 * prod1
    return  final_prod

a = [int(x) for x in input().split()]
len1 = len(a)
prod = 1

lst = []
for j in range(len1):
    lst.append(until_index(j,len1,a))

print(lst)



