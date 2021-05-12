import math
import os
import random
import re
import sys
from collections import Counter

# Complete the commonChild function below.
def commonChild(s1, s2):
    sum =0
    c1 = Counter(s1)
    c2=Counter(s2)
    intersect = []
    for item in c1.keys():
        if item in c2.keys():
            intersect.append(item)


    for ritem in intersect:
        if(c1[ritem]>c2[ritem]):
            sum = sum+c2[ritem]
        elif (c1[ritem] <= c2[ritem]):
            sum = sum + c1[ritem]

    return sum


if __name__ == '__main__':


    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)