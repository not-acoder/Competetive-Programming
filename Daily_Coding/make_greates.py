lst=list(map(str,input().split()))
one=[i for i in lst if i[0]=='1']
two=[i for i in lst if i[0]=='2']
three=[i for i in lst if i[0]=='3']
four=[i for i in lst if i[0]=='4']
five=[i for i in lst if i[0]=='5']
six=[i for i in lst if i[0]=='6']
seven=[i for i in lst if i[0]=='7']
eight=[i for i in lst if i[0]=='8']
nine=[i for i in lst if i[0]=='9']
all=[one,two,three,four,five,six,seven,eight,nine]
for i in all:
    for j in range(len(i)):

