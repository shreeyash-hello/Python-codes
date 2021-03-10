import math
import os
import random
import re
import sys
def solve(n):
    for i in n.split():
        n = n.replace(i,i.capitalize())
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
