#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    print(ct_a,ct_b)
    ct_a.subtract(ct_b)
    print(ct_a)

    return sum(abs(i) for i in ct_a.values())



if __name__ == '__main__':


    a = input()

    b = input()
    result=makeAnagram(a,b)
    print(result)




