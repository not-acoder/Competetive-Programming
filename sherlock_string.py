

def isValid(s):
    lst = []
    temp = []

    for i in s:
        y = i
        lst.append(y)
    st = set(lst)

    for j in st:
        count1 = s.count(j)
        temp.append(count1)

    temp.sort()
    print(temp)
    if(temp[-1]==temp[0]):print('YES')
    elif((temp[-1]-temp[-2]==1) and (temp[-2]==temp[0])):print('YES')
    elif ((temp[0]==1) and (temp[1]) == temp[-1]):
        print('YES')
    else:print('NO')

if __name__ == '__main__':


    s = input()

    result = isValid(s)


