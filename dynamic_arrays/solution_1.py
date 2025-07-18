#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    lastAnswer = 0
    result = []
    """ >>>1
        idx = 0
        lastAnswer = 0
        arr[0] = [5]
        arr[1] = []
        >>>2
        idx = 1
        lastAnswer = 0
        arr[0] = [5]
        arr[1] = [7]
        >>>3
        idx = 0
        lastAnswer = 0
        arr[0] = [5, 3]
        arr[1] = [7]
        >>>4
        idx = 1
        lastAnswer = 7
        arr[0] = [5, 3]
        arr[1] = [7]
        >>>5
        idx = 6
        
    """
    for query in queries:
        query_type = query[0]
        
        idx = query[1] ^ lastAnswer

        if query_type == 1:
            arr[idx].append(query[2])
        elif query_type == 2:
            lastAnswer = arr[idx][query[2]%len(arr[idx])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
