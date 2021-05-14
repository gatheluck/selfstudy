#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length_arr: int = len(arr)
    num_positive: int = 0
    num_negative: int  = 0
    num_zero: int = 0

    for value in arr:
        if value > 0:
            num_positive += 1
        elif value < 0:
            num_negative += 1
        else:
            num_zero += 1

    print("{:.6f}".format(num_positive / length_arr))
    print("{:.6f}".format(num_negative / length_arr))
    print("{:.6f}".format(num_zero / length_arr))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)