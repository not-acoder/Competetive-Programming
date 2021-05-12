def hello(num):
    flag = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return  False
                break
        else:
            return  flag
    else:
        return False

n = int(input())
answers=[]
for i in range(1,n):
    check_i=hello(i)
    if(check_i):
        for j in range(i,n):
            check_j = hello(j)
            if(check_j):
                if i+j == n:
                    answers.append([i,j])

answers.sort()
print(answers)
print(answers[0])