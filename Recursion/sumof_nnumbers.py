def func(n):
    if n==1:
        return 1
    else:
        return func(n-1)+n

result=func(3)
print(result)