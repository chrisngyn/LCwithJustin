"""
MAXIMUM CONTIGUOUS SUBARRAY

Given an array of positive numbers and a positive number ‘k’, 
find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""

from typing import List

def maximum_contiguous_subarray(arr: List[int], k: int) -> int:
    ret = 0
    window_sum, window_start = 0, 0

    for window_end in range(len(arr)):  # [0, 1, 2, 3, 4, 5] --> [0, 1, 2] --> [0, 1, 2, 3]
        window_sum += arr[window_end]   # [2, 1, 5, 1, 3, 2]

        if window_end >= k - 1:  # will ALWAYS be true past 3 tbh lol
            if window_sum > ret:
                ret = window_sum
            
            window_sum -= arr[window_start]
            window_start += 1
    
    return ret

print(maximum_contiguous_subarray([2, 1, 5, 1, 3, 2], 3))

"""
2
2 1
2 1 5
1 5
1 5 1
5 1
5 1 3
1 3
1 3 2
3 2
2
"""