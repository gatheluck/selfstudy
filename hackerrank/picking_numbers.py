#!/bin/python3

import math
import os
import random
import re
import sys
import collections
from typing import Dict, List, Tuple

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a: List[int]):
    # Write your code here
    counter_dict: Dict[int, int] = collections.Counter(a)
    counter_list: List[Tuple[int, int]] = sorted([(k, v) for k, v in counter_dict.items()], key = lambda x: x[0])
    
    max_length: int = 0
    for a, b in zip(counter_list[:-1], counter_list[1:]):
        if (abs(a[0] - b[0]) == 1) and (a[1] + b[1] > max_length):
            max_length = a[1] + b[1]

    return max_length
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
