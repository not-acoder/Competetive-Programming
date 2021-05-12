def func(n):
    if n==0:
        return 1
    else:
        return func(n-1)*n



result=func(5)
print(result)