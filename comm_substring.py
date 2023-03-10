"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.
Example:
s1 = 'and'
s2 = 'art'
These share the common substring a.
s1 = 'be'
s2 = 'cat'
These do not share a substring.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
"""
Approach: 
1. Iterate through each character in the first string.
2. For each character, check if it appears in the second string. If it does, return "YES" since there is a common substring.
3. If you iterate through the entire first string and do not find any common characters in the second string, return "NO" since there is
   no common substring. 
"""

"""
Approach: 
1. Iterate through each character in the first string.
2. For each character, check if it appears in the second string. If it does, return "YES" since there is a common substring.
3. If you iterate through the entire first string and do not find any common characters in the second string, return "NO" since there is
   no common substring. 
"""

"""
Approach: 
1. Iterate through each character in the first string.
2. For each character, check if it appears in the second string. If it does, return "YES" since there is a common substring.
3. If you iterate through the entire first string and do not find any common characters in the second string, return "NO" since there is
   no common substring. 
"""

"""
Approach: 
1. Iterate through each character in the first string.
2. For each character, check if it appears in the second string. If it does, return "YES" since there is a common substring.
3. If you iterate through the entire first string and do not find any common characters in the second string, return "NO" since there is
   no common substring. 
"""

def twoStrings(s1, s2):
    for char in s1:
        if char in s2:
            return "YES"
    return "NO"
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)
