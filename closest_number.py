#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    equal = []
    Min = abs(arr[1] - arr[0])
    for i in range(len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if diff == Min:
            equal.append([arr[i], arr[i + 1]])
        elif diff < Min:
            Min = diff
            equal.clear()
            equal.append([arr[i], arr[i + 1]])

    for i in equal:
        print(i[0], i[1], sep=" ")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    closestNumbers(arr)
