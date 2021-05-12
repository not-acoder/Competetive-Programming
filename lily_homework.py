#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
def lilysHomework(arr):
    simp = sorted(arr)
    rev = sorted(arr, reverse=True)
    swap = 0
    correct_sim = 0
    correct_rev = 0
    sim_indices = []
    rev_indices = []
    for i in arr:
        if arr.index(i) == simp.index(i): correct_sim += 1
        if arr.index(i) == rev.index(i): correct_rev += 1
        if arr.index(i) != simp.index(i): sim_indices.append(i)
        if arr.index(i) != rev.index(i): rev_indices.append(i)

    if (correct_sim >= correct_rev):
        for r in arr:
            if arr.index(r) != simp.index(r):
                arr[arr.index(r)], arr[simp.index(r)] = arr[simp.index(r)], arr[arr.index(r)]
                swap += 1
    elif (correct_sim < correct_rev):
        for r in arr:
            if arr.index(r) != rev.index(r):
                arr[arr.index(r)], arr[rev.index(r)] = arr[rev.index(r)], arr[arr.index(r)]
                swap += 1
    return swap


if __name__ == '__main__':


    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    print(result)
