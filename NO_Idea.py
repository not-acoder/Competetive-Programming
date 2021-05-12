nnm = []
nnm = input().split()
tch = []
tch = input().split()
tch = set(tch)
tch = list(tch)
A = []
A = input().split()
B = []
B = input().split()
k=0
for i in range(len(tch)):
    if tch[i] in A:
        k=k+1
    elif tch[i] in B:
        k=k-1
print(k)