"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Pseudocode #1:

- we always add the next character, store to a dictionary
- while dictionary size > k, pop off

def lengthOfLongestSubstring(s):
    ret, win_start = 0, 0
    dic = {}

    for win_end in range(len(s)):
        ch = s[win_end]

        if ch not in dic:
            dic[ch] = 0
        
        dic[ch] += 1

        if ch in dic:
"""

def lengthOfLongestSubstring(s: str) -> int:
    