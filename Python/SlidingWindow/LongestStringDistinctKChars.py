"""
Given a string, find the length of the longest substring 's' that contains at most k distinct characters.

Input: s = "eceba", k = 2
Output: 3
Explanation: s is "ece" which its length is 3.

Input: s = "aa", k = 1
Output: 2
Explanation: s is "aa" which its length is 2.


PSEUDO CODE #1:

always increase the window, and based on some conditional, determine if you should shrink the window or not

seen_char = set()
current_string
window_start = 0
num_unique_atm = 0

for each char in string:
    current_string += char

    if char is in set:
        
    else:
        seen_char.add(char)
        num_unique_atm += 1
    
    if num_unique_atm >= k:
        current_string -= string[window_start]


SUDO CODE #2:

what is the condition we want to satisfy - longest SS
what is the condition we will continue to expand our window - if we aren't at K, keep increasing
if we are at k, can we keep adding letters (without increasing k)?
if you're at k, and can't add more letters without increasing k, begin to shrink the window.


def function(s, k):
    ret = 0
    win_start = 0
    win_sum = ''
    num_unique = 0  # compare this with k


    for char in s:
        if char in win_sum:
            num_unique == num_unique
        else:
            num_unique += 1
        
        win_sum += char

        if num_unique < k:
            kk
        
        if num_unique == k:
            ret = max(ret, len(win_sum))

        while num_unique > k:  # KEEP POPPING SHIT OFF
            tbr = win_sum[win_start]
            win_sum = win_sum[win_start+1:]

            if tbr in win_sum:
                num_unique = num_unique
            else:
                num_unique -= 1
            
            win_start += 1


SUDO CODE #3

what do we know?
- always increase the window, and based on some conditional, determine if you should shrink the window or not
- what is the condition we want to satisfy: the longest substring (length)
- what condition will we continue to expand our window: if we're beneath K
- if we are at K, what do we want to do: see if you can keep expanding without going over K & set return variable
- if we are over K, what do we want to do: pop letters off until you're at K again
- no DS O(n^2) <-- strings are immutable, dict O(n) time and space

del letter_freq[key] <-- delete key in dict

def function(s, k):
    ret = 0
    win_start = 0
    letter_freq = {}

    for index in range(len(s)):
        char = s[index]

        if char in letter_freq:
            letter_freq[char] += 1
        else:
            letter_freq[char] = 1
        
        if len(letter_freq) == k:
            ret = max(ret, (index - win_start + 1))

        while len(letter_freq) > k:
            if letter_freq[s[win_start]] > 1:
                letter_freq[s[win_start]] -= 1
            else:
                del letter_freq[s[win_start]]
            
            win_start += 1
"""


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    ret, win_start = 0, 0
    letter_freq = {}  # if you had win_sum = '', appending to a string is like O(n) or some shit so use a dict instead

    for index in range(len(s)):  # access the string by its indices, 'eceba' --> [0, 1, 2, 3, 4]
        char = s[index]

        # if char in letter_freq:  # always add to your window
        #     letter_freq[char] += 1
        # else:
        #     letter_freq[char] = 1

        if char not in letter_freq:
            letter_freq[char] = 0
        
        letter_freq[char] += 1
        
        # if len(letter_freq) == k:  # case 1: you have K number of unique letters        <-- this is what happens when u dont read the question
            # ret = max(ret, index - win_start + 1)
        
        while len(letter_freq) > k:  # case 2: you have more unique letters than K
            # if (letter_freq[s[win_start]]) > 1:
            #     letter_freq[s[win_start]] -= 1
            # else:
            #     del letter_freq[s[win_start]]

            letter_freq[s[win_start]] -= 1  # alt way to do this too lol

            if letter_freq[s[win_start]] == 0:
                del letter_freq[s[win_start]]
            
            win_start += 1
        
        ret = max(ret, index - win_start + 1)  # at MOST 'k' distinct characters, you can have less, so just always check while not greater than
    
    return ret


test1 = "eceba"
print(lengthOfLongestSubstringKDistinct(test1, 2))  # expect 3
test2 = "aa"
print(lengthOfLongestSubstringKDistinct(test2, 1))  # expect 2
test3 = "a"
print(lengthOfLongestSubstringKDistinct(test3, 2))  # expect 1