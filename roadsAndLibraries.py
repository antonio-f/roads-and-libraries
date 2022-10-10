#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

from collections import defaultdict

def roadsAndLibraries(n, c_lib, c_road, cities):
    
    # Depth First Search
    def dfs(i):
        visited.add(i)
        count = 1
        if i in d:
            for j in d[i]:
                if j not in visited:
                    count+=dfs(j)
        return count

    # If roads cost more than libraries, then 
    # build n libraries 
    if c_road > c_lib:
        return c_lib*n
    visited = set()

    # build adjacency dictionary from roads
    d = defaultdict(list)
    for u, v in cities:
        d[u].append(v)
        d[v].append(u)

    # determine the number of connected components
    cc=[]
    for i in range(1, n+1):
        if i not in visited:
            cc.append(dfs(i))
    return n*c_road + (c_lib-c_road) * len(cc)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print("cost", result)
    #     fptr.write(str(result) + '\n')

    # fptr.close()