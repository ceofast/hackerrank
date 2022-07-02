# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example

# a = [1,2,3,4,3,2,1]
# The unique element is 4.
# Function Description
# Complete the lonelyinteger function in the editor below.
# lonelyinteger has the following parameter(s):
# * int a[n]: an array of integers
# Returns
# * int: the element that occurs only once.
# Input Format
# The fist line contains a single integer, n, the number of integers in the array.
# The second line contains  space-separated integers that describe the values in a.
# Constraints
# 1 <= n < 100
# It is guaranteed that n is an odd number and that there is one unique element.
# 0 <= a[i] <= 100, where 0 <= i < n.


#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    return 2 * sum(set(a)) - sum(a)
a = [1,2,3,4,3,2,1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix arr is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9
#
# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute
# difference is |15 - 17| = 2.
# Function description
# Complete the diagonalDifference function in the editor below.
# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers
# Return
# int: the absolute diagonal difference
# Input Format
# The first line contains a single integer n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row,arr[i], and consists of  space-separated integers arr[i][j].
# Constraints
# -100 <= arr[i][j] <= 100
# Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
# Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output
# 15
# Explanation
# The primary diagonal is:
# 11
#   5
#    -12
# Sum across the primary diagonal: 11 + 5 -12 = 4
# The secondary diagonal is:
#     4
#   5
# 10
# Sum across the secondary diagonal 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15
# Note: |x| is the absolute value of x.

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The dunction is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x][x] for x in range(len(arr))])
    d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    return(abs(d1 - d2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

# Quicksort usually has a running time of n * log(n), but is there an algorithm that can sort even faster?
# In general, this is not possible. Most sorting algorithms are comparison sorts,
# i.e. they sort a list just by comparing the elements to one another.
# A comparison sort algorithm cannot beat n * log(n) (worst-case) running time, since x * log(n) represents
# the minimum number of comparisons needed to know where to place each element. For more details, you can see
# these notes (PDF).
#
# Alternative Sorting
# Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array
# whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original
# array, you increment the counter at that index. At the end, run through your counting array, printing the value of
# each non-zero valued index that number of times.
#
# Example
#
# arr = [1, 2, 3, 2, 1]
# All of the values are in the range [0...3], so create an array of zeros, result = [0, 0, 0, 0]. The results of each
# iteration follow:
# i     arr[i]     result
# 0     1          [0, 1, 0, 0]
# 1     1          [0, 2, 0, 0]
# 2     3          [0, 2, 0, 1]
# 3     2          [0, 2, 1, 1]
# 4     1          [0, 3, 1, 1]
#
# The frequnecy array is [0, 3, 1, 1]. These values can be used to create the sorted array as well:
# sorted = [1, 1, 1, 2, 3].
#
# Note
#
# For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements,
# the remainder being zeros.
#
# Challenge
#
# Given a list of integers, count and return the number of times each value appears as an array of integers.
#
# Function Description
#
# Complete the countingSort function in the editor below.
# countingSort has the following parameter(s):
# arr[n]: an array of integers
#
# Returns
#
# int[100]: a frequency array
#
# Input Format
#
# The first line contains an integer n, the number of items in arr.
# Each of the next n lines contains an integer arr[i] where 0 <= i <= n.
#
# Constraints
#
# 100 <= n <= 10^6
# 0 <= arr[i] <= 100
#
# Sample Input
#
# 100
# 63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33
#
# Sample Output
#
# 0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2
#
# Explanation
#
# Each of the resulting values result[i] represents the number of times i appeared in arr.

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result = [0]*100
    for i in arr:
        # print(i)
        result[i] += 1
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()