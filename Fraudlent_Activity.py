#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d ,n):
    temp = []
    count = 0
    for i in range(n):

        try:
            for j in range(i,i+d):
                temp.append(expenditure[j])

            #print(temp)

        except:
            pass;
        a = statistics.median(temp)
        #print(a)

        try:
            #print(expenditure[i+d])
            if(a*2<=expenditure[i+d]):
                count+=1
                #print(str(count)+" hello")

        except:
            pass
        temp = []

    return count


if __name__ == '__main__':


    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d ,n)
    print(result)


