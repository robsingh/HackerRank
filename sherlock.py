"""Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Returns:
int: the number of unordered anagrammatic pairs of substrings in 
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a string  to analyze."""

#!/bin/python3
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def sherlockAndAnagrams(s:str) -> int:
    """
    Counts the number of pair of substrings of s that are anagrams of each other.
    Args:
        s : str: input string
    Returns:
        int: the number of pairs of anagram substrings"""
    
    freq = {}
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            # calculate the frequency of characters in the substring 
            sub_freq = {}
            for c in s[i:j+1]:
                sub_freq[c] = sub_freq.get(c,0) + 1

            # check if any previous substring has the same frequency of characters
            for f in freq:
                if freq[f] == sub_freq:
                    count += 1
            # add the frequency of this substring to the hash map
            freq[(i,j)] = sub_freq
    return count

if __name__ == '__main__':
    fptr = open("output.txt",'w')
    while True:
        try:
            s = input()
            result = sherlockAndAnagrams(s)
            fptr.write(str(result) + "\n")
        except EOFError:
            break

    fptr.close()

