"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. 
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must use only whole words available in the magazine. 
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Example:
magazine="attack at dawn" note="Attack at dawn"
The magazine has all the right words, but there is a case mismatch. The answer is NO.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # create a dictionary to count the frequency of each word in the magazine
    word_count = {}
    for word in magazine:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # check whether each word in the note is in the dictionary and has a count greater than zero
    for word in note:
        if word in word_count and word_count[word] > 0:
            word_count[word] -= 1
        else:
            print("No")
            return
    print("Yes")




if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)