"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t.
If there is no such window in s that covers all characters in t, return the empty string "".

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"


approach - let's say 't' is 'aabb', so we have 4 characters to match. we'll keep a variable 'matched_char' that we increment when we visit a letter we need.
once matched_char == len(t), we'll start popping off characters until we pop off one we need, where matched_char is decremented
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_dict = Counter(t)
        matched_char = 0  # need to match len(t)
        substr_str = 0  # where does the substring start? how long is it? this is what we need so we can return something in the end
        substr_len = float('inf')
        win_str = 0
        
        for win_end in range(len(s)):
            char = s[win_end]
            
            if char in char_dict:
                char_dict[char] -= 1
                
                if char_dict[char] >= 0:  # if 's' is 'aaaa' and 't' is 'aa', our count would go to -2. meaning we have more characters than needed
                    matched_char += 1
                    
            while matched_char == len(t):
                if win_end - win_str + 1 < substr_len:  # if window length is smaller than what we currently have, set the length, and set where it begins
                    substr_str = win_str
                    substr_len = win_end - win_str + 1
                    
                ch = s[win_str]
                
                if ch in char_dict:
                    if char_dict[ch] >= 0:
                        matched_char -= 1
                    
                    char_dict[ch] += 1
                
                win_str += 1
        
        if substr_len == float('inf'):
            return ''
        
        return s[substr_str : substr_str + substr_len]
