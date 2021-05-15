#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s.endswith("AM"):
        if s.startswith("12"):
            return "{hour}:{min}:{sec}".format(hour="00", min=s[3:5], sec=s[6:8])
        else:
            return "{hour}:{min}:{sec}".format(hour=s[0:2], min=s[3:5], sec=s[6:8])
    else:
        if s.startswith("12"):
            return "{hour}:{min}:{sec}".format(hour=s[0:2], min=s[3:5], sec=s[6:8])
        else:
            return "{hour:02d}:{min}:{sec}".format(hour=int(s[0:2])+12, min=s[3:5], sec=s[6:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
