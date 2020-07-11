"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.
"""

def firstNotRepeatingCharacter(s):
    char_freq = {}
    # char_freq = collections.Counter(s)
    
    for char in s:
        if char not in char_freq:
            char_freq[char] = 0
        
        char_freq[char] += 1
    
    for char in s:
        if char_freq[char] == 1:
            return char
    
    return '_'

t1 = 'abacabad'
print(firstNotRepeatingCharacter(t1))