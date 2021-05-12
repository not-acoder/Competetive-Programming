
def func(n,memo):
    if memo[n]!=-1:
        return memo[n]
    if n<=1:
        return n
    else:
        memo[n]=func(n-2,memo)+func(n-1,memo)
        return memo[n]


n=int(input())
memo = [-1] * (n + 1)
memo[0] = 0
memo[1] = 1
memo[2] = 1

result=func(n,memo)
print(result)



