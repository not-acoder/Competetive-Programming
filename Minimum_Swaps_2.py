#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    temp = [None]*len(arr)
    res1=sorted(arr)
    #res1.sort()
    print(arr)

    while(res1!=arr):
        for i in range(int(len(arr))):
            if(res1[i]!=arr[i]):
               y=res1.index(arr[i])
               #print(y)
               arr[y] , arr[i]=arr[i] , arr[y]
               count = count +1

    print(arr)
    return count

if __name__ == '__main__':


    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)




