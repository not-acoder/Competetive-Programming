import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    print(prices)
    sum1=0
    lst = []

    for i in prices:
        if (sum1<k):
            lst.append(i)
            sum1=sum(lst)
            print(sum1)
    if(sum1>k):
        lst.remove(lst[-1])
    print(lst)
    return (len(lst))


if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)
