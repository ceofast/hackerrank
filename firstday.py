#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    x,z,y = 0,0,0
    for i in range(0, len(arr)):
        if arr[i]>0:
            x = x + 1
        elif arr[i]<0:
            y = y + 1
        else:
            x = z + 1
    print(x/len(arr))
    print(y/len(arr))
    print(z/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    hold = [None] * int(len(arr) - 3)
    for i in range(0, len(arr) - 3):
        temp = 0
        for j in range(i, i + 4):
            temp = temp + arr[j]
        hold[i] = temp

    print(hold[0], hold[-1])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# !/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        ans = int(s[:2]) + 12
        return str(str(ans) + s[2:8])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(str(result) + '\n')

    f.close()