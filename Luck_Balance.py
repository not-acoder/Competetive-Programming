#!/bin/python

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    # sort from greatest luck to least luck
    contests.sort(reverse=True)
    luck = 0

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]

    return luck

if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(map(int, input().rstrip().split()))

    result = luckBalance(k, contests)

