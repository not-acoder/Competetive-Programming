string = input()
lst = list(string)
final=''
for i in range(0,len(lst),2):
    lst[i] , lst[i+1]=lst[i+1] , lst[i]

for i in lst:
    final+=i
print(final)