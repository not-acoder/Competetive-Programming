#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):

    temp = [0] * n
    temp[0] = 1
    try:
        for i in range(1, n):
            if (arr[i] > arr[i - 1]):
                temp[i] = temp[i - 1] + 1
            elif (arr[i] < arr[i - 1]):
                if (arr[i - 1] > arr[i - 2]):
                    temp[i] = 1
                elif (arr[i - 1] < arr[i - 2]):
                    temp[i - 1] = temp[i - 1] + 1
                    temp[i] = 1

            elif (arr[i] == arr[i - 1]):
                temp[i] = 1
    except:
        pass;
    return sum(temp)


if __name__ == '__main__':


    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    print(result)
