#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum1 = []

    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            y = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2]
            [j + 1] + arr[i + 2][j + 2])
            sum1.append(y)
            y = 0

    print(max(sum1))


if __name__ == '__main__':


    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)


