# cook your dish here
if __name__ == "__main__":
    flag = False
    error = 0
    t = int(input())
    for i in range(t):
        n = int(input())
        lst = list(input().split(" "))
        for j in lst:
            if j == 'start':
                flag = True
            elif j == 'restart':
                flag = True
            elif j == 'stop' and flag == False:
                error = 1
                break
            elif j == 'stop' and flag == True:
                flag = False

        if error==0:
            print(200)

        else:
            print(404)
