#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    lst = 'abcdefghijklmnopqrstuvwxyz'
    weights = []
    same = ''
    for i in set(s):
        weights.append(lst.index(i) + 1)
    # print(weights)
    try:
        for i in range(len(s)):
            j = i + 1
            r = 2
            flag = True
            while (flag == True):
                if s[i] == s[j]:
                    weights.append((lst.index(s[i]) + 1) * r)
                    r += 1
                    j += 1
                else:
                    flag = False
            i = j
    except IndexError:
        pass

    # print(weights)
    for i in queries:
        if i in weights:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    weightedUniformStrings(s, queries)


