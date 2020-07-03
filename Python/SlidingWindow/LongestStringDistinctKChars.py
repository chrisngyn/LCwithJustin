"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.


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
"""

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    


test1 = "eceba"
print(lengthOfLongestSubstringKDistinct(test1, 2))
test2 = "aa"
print(lengthOfLongestSubstringKDistinct(test2, 1))
