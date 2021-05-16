#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year: int):
    # Write your code here
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    if year == "1918":
        num_days[2] = 15
    elif (year < 1918) and (year % 4 == 0):
        num_days[2] = 29
    elif (year > 1918) and ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        num_days[2] = 29

    counter = 256
    for m, num_days in num_days.items():
        if counter <= num_days:
            print("{day:02d}.{month:02d}.{year:4d}".format(day=counter, month=m, year=year))
            break
        else:
            counter -= num_days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
