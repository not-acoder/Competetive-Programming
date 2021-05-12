#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    #print(c)
    dist=[]
    for i in range(n):
        #print(i)
        if i in c:

            dist.append(0)
        elif (i-1 in c) or (i+1 in c):
            #print(i,i+1,i-1)
            dist.append(1)
        else:
            for j in range(2,n):
                if (i+j in c)or (i-j in c):
                    print(i,j)
                    dist.append(j)
                    break
        #print(dist)
    return max(dist)
if __name__ == '__main__':


    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)
