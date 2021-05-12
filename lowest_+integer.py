lst = [int(x) for x in input().split()]
lst.sort()
for i in range(lst[0],lst[-1]+2):
    if ((i in lst) or (i<=0)):
        pass;
    else:
        print('the missing character is'+ str(i) )
        break;