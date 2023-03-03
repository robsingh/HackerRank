"""
Given a string, check if it is a palindrome permutation.
	str1 = "ab"; // false
	str2 = "cba"; // false
	str3 = "aba"; // true
	str4 = "aab"; // true
"""
"""
Palindrome is a word, phase or a sentence that reads the same forward and backward.
A palindrome permutation is a string that can be rearranged to form a palindrome.
It should meet ONE of the following conditions:
1. All characters in the string occur an even number of times.
2. One character occurs an odd number of times, while all other characters occur an even number of times.
"""
"""
Time complexity is O(n) because the function iterate over the string once to build the character count dictionary
and then iterates over the values in the dictionary once to check if there is atmost one character with an odd count.

Space complexity is also O(n) because in the worst case, every character in the input string could be unique,which would
require creating a new key-pair value pair in the character count dictionary for each character in the string.

"""

def is_palindrome_permutation(s):
    # Remove any spaces in the string and convert to lowercase
    string = s.replace(" ","").lower()

    #create a dictionary to track the character counts
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    
    # check if atmost one character has an odd count
    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
        
    return True

str1 = 'ab'
str2 = 'cba'
str3 = 'aba'
str4 = 'aab'


print(is_palindrome_permutation(s=str1))
print(is_palindrome_permutation(s=str2))
print(is_palindrome_permutation(s=str3))
print(is_palindrome_permutation(s=str4))