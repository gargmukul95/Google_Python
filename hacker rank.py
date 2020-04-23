#!/bin/python3

import math
import os
import random
import re
import sys


# n = int(sys.stdin.readline())
# print(n)
def weird(n):
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and 1 < n < 5:
        print('Not Weird')
    elif n % 2 == 0 and 5 < n < 21:
        print('Weird')
    else:
        print('Not Weird')


if __name__ == '__main__':
    N = int(input())
    weird(N)
