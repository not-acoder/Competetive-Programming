#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    st = set(brr)
    temp = []
    for i in st:
        if (arr.count(i) != brr.count(i)):
            temp.append(i)
    temp.sort()
    print(*temp)
    print(arr.count(3685),brr.count(3685))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    missingNumbers(arr, brr)

