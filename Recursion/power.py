def func(m,n):
    if n==0:
        return 1

    else:
        return func(m,n-1)*m



result=func(9,9)
print(result)