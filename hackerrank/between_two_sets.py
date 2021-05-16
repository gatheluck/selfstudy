#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List
from collections import Counter

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here

    def prime_factorize(n: int) -> List[int]:
        if n == 1:
            return [1]

        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    lcm = math.lcm(*a)
    gcd = math.gcd(*b)

    count = Counter(prime_factorize(gcd / lcm))

    num_between_sets: int = 1

    for v in count.values():
        num_between_sets *= (v + 1)

    return num_between_sets
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()