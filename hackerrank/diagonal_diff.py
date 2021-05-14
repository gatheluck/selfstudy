#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_diagonal: int = 0
    secondary_diagonal: int = 0
    
    n: int = len(arr)    

    for i, ith_row in enumerate(arr):
        primary_diagonal += ith_row[i]
        secondary_diagonal += ith_row[n-1-i]

    return abs(primary_diagonal - secondary_diagonal)
    

if __name__ == '__main__':
    # export OUTPUT_PATH=output/out.txt
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()