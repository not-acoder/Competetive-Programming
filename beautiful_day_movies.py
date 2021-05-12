import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
def beautifulDays(i, j, z):
    count = 0
    for r in range(i, j + 1):
        k = str(r)
        l = "".join(reversed(k))

        a = (abs(int(k) - int(l))) / z

        if (a == math.floor(a)):
            count += 1
    return count


if __name__ == '__main__':


    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    z = int(ijk[2])

    result = beautifulDays(i, j, z)

    print(result)

