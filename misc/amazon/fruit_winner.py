#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY codeList
#  2. STRING_ARRAY shoppingCart
#
'''
[[apple, apple], [banana, anything, banana]]
'''


def check_fruit_seq(i, shoppingCart, codeList, group):
    expected = codeList[group].split(" ")
    # print(expected)
    j = i
    k = 0

    while k < len(expected):
        if j == len(shoppingCart) or expected[k] != shoppingCart[j]:
            if expected[k] != "anything":
                return -1
        k += 1
        j += 1

    return len(expected)


def foo(codeList, shoppingCart):
    if len(codeList) == 0:
        return 0
    i = 0
    group = 0
    while i < len(shoppingCart):
        count = check_fruit_seq(i, shoppingCart, codeList, group)
        if count == -1:
            i += 1
            continue
        else:
            i += count
            group += 1
    return 1 if group == len(codeList) else 0

