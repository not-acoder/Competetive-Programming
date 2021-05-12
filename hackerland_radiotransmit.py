#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    a = [0] * (len(x) + 1)
    count = 0
    for i in x:
        a[i] = 1
    j = 0
    while (j < len(x) + 1):
        if a[j] == 0:
            j += 1
            pass
        else:
            try:
                if a[j + k] == 1:
                    # count+=1
                    j = j + k
                elif a[j + k] == 0:
                    temp = j + k - 1
                    while (temp > j):
                        if a[temp] == 1:
                            # count+=1
                            j = temp
                            break
                        elif a[temp] == 0:
                            temp -= 1
                    else:
                        j = j + k + 1
            except IndexError:
                pass;

            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
